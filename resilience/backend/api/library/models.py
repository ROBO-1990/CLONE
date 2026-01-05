from django.db import models
from django.contrib.auth.models import User


class ResourceCategory(models.Model):
    """Catégories de ressources"""
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Resource Categories"
        ordering = ['name']

    def __str__(self):
        return self.name


class Resource(models.Model):
    """Rapports, guides, outils téléchargeables"""
    RESOURCE_TYPES = [
        ('report', 'Rapport'),
        ('guide', 'Guide pratique'),
        ('policy', 'Politique'),
        ('tool', 'Outil technique'),
        ('data', 'Données ouvertes'),
        ('scientific', 'Article scientifique'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    resource_type = models.CharField(max_length=20, choices=RESOURCE_TYPES, default='report')
    file = models.FileField(upload_to='library/resources/')
    thumbnail = models.ImageField(upload_to='library/thumbnails/', blank=True, null=True)
    
    # Métadonnées
    category = models.ForeignKey(ResourceCategory, on_delete=models.SET_NULL, null=True, blank=True)
    author = models.CharField(max_length=200, blank=True)
    organization = models.CharField(max_length=200, blank=True, help_text="ONU, IFRC, Banque Mondiale, etc.")
    publication_date = models.DateField(null=True, blank=True)
    language = models.CharField(max_length=10, default='fr')
    
    # Statistiques
    download_count = models.PositiveIntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-publication_date', '-created_at']

    def __str__(self):
        return self.title

    def increment_download(self):
        """Incrémente le compteur de téléchargements"""
        self.download_count += 1
        self.save(update_fields=['download_count'])
