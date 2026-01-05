from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FirstAidGuideViewSet, FirstAidVideoViewSet, QuizViewSet, BadgeViewSet

router = DefaultRouter()
router.register(r'guides', FirstAidGuideViewSet, basename='firstaid-guide')
router.register(r'videos', FirstAidVideoViewSet, basename='firstaid-video')
router.register(r'quiz', QuizViewSet, basename='quiz')
router.register(r'badges', BadgeViewSet, basename='badge')

urlpatterns = [
    path('', include(router.urls)),
]
