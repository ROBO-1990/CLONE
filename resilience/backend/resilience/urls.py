"""
URL configuration for resilience project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from django.http import JsonResponse

def health_check(request):
    """Simple health check endpoint that doesn't require database"""
    return JsonResponse({'status': 'healthy', 'service': 'resilience-backend'})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health_check, name='health-check'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/articles/', include('api.articles.urls')),
    path('api/content/', include('api.content.urls')),
    path('api/multimedia/', include('api.multimedia.urls')),
    path('api/first-aid/', include('api.first_aid.urls')),
    path('api/library/', include('api.library.urls')),
    path('api/users/', include('api.users.urls')),
    path('api/contact/', include('api.contact.urls')),
    path('api/maps/', include('api.maps.urls')),
    path('api/search/', include('api.search.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
