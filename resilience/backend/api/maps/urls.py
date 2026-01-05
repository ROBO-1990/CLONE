from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RiskZoneViewSet, AlertViewSet

router = DefaultRouter()
router.register(r'risk-zones', RiskZoneViewSet, basename='risk-zone')
router.register(r'alerts', AlertViewSet, basename='alert')

urlpatterns = [
    path('', include(router.urls)),
]
