from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.http import FileResponse
from .models import Resource, ResourceCategory
from .serializers import ResourceSerializer, ResourceListSerializer, ResourceCategorySerializer


class ResourceCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ResourceCategory.objects.all()
    serializer_class = ResourceCategorySerializer
    lookup_field = 'slug'


class ResourceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Resource.objects.filter(published=True).select_related('category')
    serializer_class = ResourceListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['resource_type', 'category', 'language']
    search_fields = ['title', 'description', 'author', 'organization']
    ordering_fields = ['publication_date', 'created_at', 'download_count', 'title']
    ordering = ['-publication_date', '-created_at']
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ResourceSerializer
        return ResourceListSerializer

    @action(detail=True, methods=['get'])
    def download(self, request, pk=None):
        """Télécharge une ressource et incrémente le compteur"""
        resource = self.get_object()
        resource.increment_download()
        
        if resource.file:
            return FileResponse(
                resource.file.open(),
                as_attachment=True,
                filename=resource.file.name.split('/')[-1]
            )
        return Response({'error': 'File not found'}, status=404)
