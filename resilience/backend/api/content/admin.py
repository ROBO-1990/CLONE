from django.contrib import admin
from .models import Dossier, DossierSection


class DossierSectionInline(admin.TabularInline):
    model = DossierSection
    extra = 1
    fields = ['title', 'content', 'image', 'order']


@admin.register(Dossier)
class DossierAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'featured', 'published', 'published_at', 'created_at']
    list_filter = ['published', 'featured', 'created_at']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at', 'updated_at']
    inlines = [DossierSectionInline]
    
    fieldsets = (
        ('Contenu', {
            'fields': ('title', 'slug', 'description', 'cover_image')
        }),
        ('Publication', {
            'fields': ('author', 'featured', 'published', 'published_at')
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at')
        }),
    )


@admin.register(DossierSection)
class DossierSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'dossier', 'order']
    list_filter = ['dossier']
    search_fields = ['title', 'content']
    ordering = ['dossier', 'order']
