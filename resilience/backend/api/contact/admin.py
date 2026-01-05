from django.contrib import admin
from .models import ContactMessage, ReporterApplication


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject_type', 'subject', 'read', 'replied', 'created_at']
    list_filter = ['subject_type', 'read', 'replied', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at']
    actions = ['mark_as_read', 'mark_as_unread', 'mark_as_replied']
    
    def mark_as_read(self, request, queryset):
        queryset.update(read=True)
    mark_as_read.short_description = "Marquer comme lu"
    
    def mark_as_unread(self, request, queryset):
        queryset.update(read=False)
    mark_as_unread.short_description = "Marquer comme non lu"
    
    def mark_as_replied(self, request, queryset):
        queryset.update(replied=True)
    mark_as_replied.short_description = "Marquer comme répondu"


@admin.register(ReporterApplication)
class ReporterApplicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'location', 'reviewed', 'created_at']
    list_filter = ['reviewed', 'created_at']
    search_fields = ['name', 'email', 'location', 'motivation']
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at']
    actions = ['mark_as_reviewed', 'mark_as_unreviewed']
    
    def mark_as_reviewed(self, request, queryset):
        queryset.update(reviewed=True)
    mark_as_reviewed.short_description = "Marquer comme examiné"
    
    def mark_as_unreviewed(self, request, queryset):
        queryset.update(reviewed=False)
    mark_as_unreviewed.short_description = "Marquer comme non examiné"
