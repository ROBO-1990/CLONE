from django.contrib import admin
from .models import Resource, ResourceCategory


@admin.register(ResourceCategory)
class ResourceCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ['title', 'resource_type', 'category', 'organization', 'download_count', 'published', 'created_at']
    list_filter = ['resource_type', 'category', 'published', 'language', 'created_at']
    search_fields = ['title', 'description', 'author', 'organization']
    date_hierarchy = 'created_at'
    readonly_fields = ['download_count']
    
    fieldsets = (
        ('Contenu', {
            'fields': ('title', 'description', 'resource_type', 'file', 'thumbnail')
        }),
        ('Organisation', {
            'fields': ('category', 'author', 'organization', 'publication_date', 'language')
        }),
        ('Statistiques', {
            'fields': ('download_count',)
        }),
        ('Publication', {
            'fields': ('published',)
        }),
    )
