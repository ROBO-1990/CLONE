from django.contrib import admin
from .models import Video, Podcast, Photo, Webinar


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'video_type', 'author', 'duration', 'published', 'created_at']
    list_filter = ['video_type', 'published', 'created_at']
    search_fields = ['title', 'description']
    date_hierarchy = 'created_at'


@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin):
    list_display = ['title', 'episode_number', 'author', 'duration', 'published', 'created_at']
    list_filter = ['published', 'created_at']
    search_fields = ['title', 'description']
    date_hierarchy = 'created_at'


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'gallery_name', 'author', 'published', 'created_at']
    list_filter = ['gallery_name', 'published', 'created_at']
    search_fields = ['title', 'description', 'gallery_name']
    date_hierarchy = 'created_at'


@admin.register(Webinar)
class WebinarAdmin(admin.ModelAdmin):
    list_display = ['title', 'speaker', 'scheduled_at', 'duration', 'published', 'created_at']
    list_filter = ['published', 'scheduled_at']
    search_fields = ['title', 'description', 'speaker']
    date_hierarchy = 'scheduled_at'
