from django.db import models
from django.contrib.auth.models import User


class Video(models.Model):
    """Vidéos pédagogiques, reportages"""
    VIDEO_TYPES = [
        ('educational', 'Pédagogique'),
        ('report', 'Reportage'),
        ('interview', 'Interview'),
        ('webinar', 'Webinaire'),
        ('testimonial', 'Témoignage'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    video_url = models.URLField()
    thumbnail = models.ImageField(upload_to='multimedia/videos/', blank=True, null=True)
    video_type = models.CharField(max_length=20, choices=VIDEO_TYPES, default='educational')
    duration = models.PositiveIntegerField(help_text="Durée en secondes", null=True, blank=True)
    
    # Métadonnées
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='videos')
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Podcast(models.Model):
    """Épisodes de podcasts"""
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    audio_url = models.URLField()
    thumbnail = models.ImageField(upload_to='multimedia/podcasts/', blank=True, null=True)
    duration = models.PositiveIntegerField(help_text="Durée en secondes", null=True, blank=True)
    episode_number = models.PositiveIntegerField(null=True, blank=True)
    
    # Métadonnées
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='podcasts')
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-episode_number', '-created_at']

    def __str__(self):
        return self.title


class Photo(models.Model):
    """Galeries photos"""
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='multimedia/photos/')
    gallery_name = models.CharField(max_length=100, blank=True)
    
    # Métadonnées
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='photos')
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Webinar(models.Model):
    """Webinaires et conférences"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_url = models.URLField(blank=True)
    thumbnail = models.ImageField(upload_to='multimedia/webinars/', blank=True, null=True)
    scheduled_at = models.DateTimeField(null=True, blank=True)
    duration = models.PositiveIntegerField(help_text="Durée en minutes", null=True, blank=True)
    
    # Métadonnées
    speaker = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-scheduled_at', '-created_at']

    def __str__(self):
        return self.title
