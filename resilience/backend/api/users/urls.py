from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from .views import UserViewSet, CommentViewSet, CustomTokenObtainPairView

router = DefaultRouter()
router.register(r'', UserViewSet, basename='user')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('auth/register/', UserViewSet.as_view({'post': 'create'}), name='register'),
    path('auth/login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
