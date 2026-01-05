from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    """Catégories pour organiser les articles"""
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name


class Tag(models.Model):
    """Tags pour organiser les articles"""
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Article(models.Model):
    """Articles, actualités, éditos, décryptages"""
    ARTICLE_TYPES = [
        ('news', 'Actualité'),
        ('editorial', 'Éditorial'),
        ('analysis', 'Décryptage'),
        ('chronicle', 'Chronique'),
        ('short', 'Article court'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    subtitle = models.CharField(max_length=300, blank=True)
    content = models.TextField()
    excerpt = models.TextField(max_length=500, blank=True)
    article_type = models.CharField(max_length=20, choices=ARTICLE_TYPES, default='news')
    
    # Relations
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='articles')
    
    # Médias
    featured_image = models.ImageField(upload_to='articles/', blank=True, null=True)
    
    # Métadonnées
    published = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)
    
    # SEO
    meta_description = models.CharField(max_length=160, blank=True)
    
    class Meta:
        ordering = ['-published_at', '-created_at']
        indexes = [
            models.Index(fields=['-published_at']),
            models.Index(fields=['published', 'featured']),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'slug': self.slug})
