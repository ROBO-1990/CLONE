from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Dossier
from .serializers import DossierSerializer, DossierListSerializer


class DossierViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Dossier.objects.filter(published=True).select_related('author').prefetch_related('sections')
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['featured']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'published_at', 'title']
    ordering = ['-published_at', '-created_at']
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return DossierSerializer
        return DossierListSerializer

    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Retourne les dossiers mis en vedette"""
        featured_dossiers = self.queryset.filter(featured=True)[:5]
        serializer = self.get_serializer(featured_dossiers, many=True)
        return Response(serializer.data)
