from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VideoViewSet, PodcastViewSet, PhotoViewSet, WebinarViewSet

router = DefaultRouter()
router.register(r'videos', VideoViewSet, basename='video')
router.register(r'podcasts', PodcastViewSet, basename='podcast')
router.register(r'photos', PhotoViewSet, basename='photo')
router.register(r'webinars', WebinarViewSet, basename='webinar')

urlpatterns = [
    path('', include(router.urls)),
]
