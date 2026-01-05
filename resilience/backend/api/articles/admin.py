from django.contrib import admin
from .models import Article, Category, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'article_type', 'category', 'author', 'published', 'featured', 'published_at', 'created_at']
    list_filter = ['article_type', 'published', 'featured', 'category', 'created_at']
    search_fields = ['title', 'content', 'excerpt']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['tags']
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Contenu', {
            'fields': ('title', 'slug', 'subtitle', 'content', 'excerpt', 'article_type')
        }),
        ('Organisation', {
            'fields': ('category', 'tags', 'author')
        }),
        ('Médias', {
            'fields': ('featured_image',)
        }),
        ('Publication', {
            'fields': ('published', 'featured', 'published_at', 'meta_description')
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at')
        }),
    )
