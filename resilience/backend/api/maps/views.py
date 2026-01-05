from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import RiskZone, Alert
from .serializers import RiskZoneSerializer, AlertSerializer


class RiskZoneViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = RiskZone.objects.filter(active=True)
    serializer_class = RiskZoneSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['risk_type', 'risk_level']
    search_fields = ['name', 'description']


class AlertViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Alert.objects.filter(active=True)
    serializer_class = AlertSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['alert_type']
    search_fields = ['title', 'message']
    ordering_fields = ['issued_at']
    ordering = ['-issued_at']

    @action(detail=False, methods=['get'])
    def active(self, request):
        """Retourne les alertes actives"""
        active_alerts = self.queryset.filter(active=True)[:10]
        serializer = self.get_serializer(active_alerts, many=True)
        return Response(serializer.data)
