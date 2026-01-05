from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Dossier(models.Model):
    """Dossiers thématiques avec sections"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='dossiers/', blank=True, null=True)
    
    # Métadonnées
    featured = models.BooleanField(default=False)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)
    
    # Relations
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='dossiers')
    
    class Meta:
        ordering = ['-published_at', '-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('dossier-detail', kwargs={'slug': self.slug})


class DossierSection(models.Model):
    """Sections d'un dossier"""
    dossier = models.ForeignKey(Dossier, on_delete=models.CASCADE, related_name='sections')
    title = models.CharField(max_length=200)
    content = models.TextField()
    order = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='dossiers/sections/', blank=True, null=True)
    
    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f"{self.dossier.title} - {self.title}"
