from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import UserProfile, Comment, SavedContent, NewsletterSubscription


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'location', 'created_at']
    search_fields = ['user__username', 'user__email', 'phone', 'location']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['article', 'user', 'approved', 'created_at']
    list_filter = ['approved', 'created_at']
    search_fields = ['content', 'user__username', 'article__title']
    date_hierarchy = 'created_at'
    actions = ['approve_comments', 'disapprove_comments']
    
    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
    approve_comments.short_description = "Approuver les commentaires sélectionnés"
    
    def disapprove_comments(self, request, queryset):
        queryset.update(approved=False)
    disapprove_comments.short_description = "Désapprouver les commentaires sélectionnés"


@admin.register(SavedContent)
class SavedContentAdmin(admin.ModelAdmin):
    list_display = ['user', 'content_type', 'content_id', 'saved_at']
    list_filter = ['content_type', 'saved_at']
    search_fields = ['user__username']
    date_hierarchy = 'saved_at'


@admin.register(NewsletterSubscription)
class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'active', 'subscribed_at', 'unsubscribed_at']
    list_filter = ['active', 'subscribed_at']
    search_fields = ['email', 'name']
    date_hierarchy = 'subscribed_at'
    readonly_fields = ['subscribed_at', 'unsubscribed_at']
