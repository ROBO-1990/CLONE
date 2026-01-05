from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Video, Podcast, Photo, Webinar
from .serializers import VideoSerializer, PodcastSerializer, PhotoSerializer, WebinarSerializer


class VideoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Video.objects.filter(published=True).select_related('author')
    serializer_class = VideoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['video_type']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'title']
    ordering = ['-created_at']


class PodcastViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Podcast.objects.filter(published=True).select_related('author')
    serializer_class = PodcastSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['episode_number', 'created_at', 'title']
    ordering = ['-episode_number', '-created_at']


class PhotoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Photo.objects.filter(published=True).select_related('author')
    serializer_class = PhotoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['gallery_name']
    search_fields = ['title', 'description', 'gallery_name']
    ordering_fields = ['created_at', 'title']
    ordering = ['-created_at']


class WebinarViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Webinar.objects.filter(published=True)
    serializer_class = WebinarSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description', 'speaker']
    ordering_fields = ['scheduled_at', 'created_at', 'title']
    ordering = ['-scheduled_at', '-created_at']
