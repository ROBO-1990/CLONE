from django.contrib import admin
from .models import RiskZone, Alert


@admin.register(RiskZone)
class RiskZoneAdmin(admin.ModelAdmin):
    list_display = ['name', 'risk_type', 'risk_level', 'latitude', 'longitude', 'active', 'created_at']
    list_filter = ['risk_type', 'risk_level', 'active', 'created_at']
    search_fields = ['name', 'description']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Informations générales', {
            'fields': ('name', 'risk_type', 'risk_level', 'description', 'active')
        }),
        ('Localisation', {
            'fields': ('latitude', 'longitude', 'area_coordinates')
        }),
        ('Actions et contacts', {
            'fields': ('preventive_actions', 'emergency_contacts')
        }),
    )


@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ['title', 'alert_type', 'risk_zone', 'active', 'issued_at', 'expires_at']
    list_filter = ['alert_type', 'active', 'issued_at']
    search_fields = ['title', 'message']
    date_hierarchy = 'issued_at'
    readonly_fields = ['issued_at']
    
    fieldsets = (
        ('Contenu', {
            'fields': ('title', 'alert_type', 'message')
        }),
        ('Localisation', {
            'fields': ('risk_zone', 'latitude', 'longitude')
        }),
        ('Dates', {
            'fields': ('issued_at', 'expires_at', 'active')
        }),
    )
