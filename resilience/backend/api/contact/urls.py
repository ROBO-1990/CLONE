from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactMessageViewSet, ReporterApplicationViewSet, NewsletterViewSet

router = DefaultRouter()
router.register(r'messages', ContactMessageViewSet, basename='contact-message')
router.register(r'reporters', ReporterApplicationViewSet, basename='reporter-application')
router.register(r'newsletter', NewsletterViewSet, basename='newsletter')

urlpatterns = [
    path('', include(router.urls)),
]
