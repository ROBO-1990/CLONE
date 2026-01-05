from django.db import models


class RiskZone(models.Model):
    """Zones à risques géographiques"""
    RISK_TYPES = [
        ('flood', 'Inondation'),
        ('earthquake', 'Séisme'),
        ('landslide', 'Glissement de terrain'),
        ('drought', 'Sécheresse'),
        ('fire', 'Incendie'),
        ('storm', 'Tempête'),
        ('volcano', 'Volcan'),
    ]

    RISK_LEVELS = [
        ('low', 'Faible'),
        ('medium', 'Moyen'),
        ('high', 'Élevé'),
        ('critical', 'Critique'),
    ]

    name = models.CharField(max_length=200)
    risk_type = models.CharField(max_length=20, choices=RISK_TYPES)
    risk_level = models.CharField(max_length=20, choices=RISK_LEVELS, default='medium')
    description = models.TextField(blank=True)
    
    # Coordonnées géographiques
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    
    # Zone (polygone GeoJSON simplifié)
    area_coordinates = models.JSONField(null=True, blank=True, help_text="Coordonnées de la zone en format GeoJSON")
    
    # Informations supplémentaires
    preventive_actions = models.TextField(blank=True, help_text="Actions préventives recommandées")
    emergency_contacts = models.JSONField(default=list, blank=True, help_text="Contacts d'urgence")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-risk_level', 'name']
        indexes = [
            models.Index(fields=['risk_type', 'risk_level']),
            models.Index(fields=['latitude', 'longitude']),
        ]

    def __str__(self):
        return f"{self.name} - {self.get_risk_type_display()} ({self.get_risk_level_display()})"


class Alert(models.Model):
    """Alertes en temps réel (optionnel)"""
    ALERT_TYPES = [
        ('warning', 'Avertissement'),
        ('watch', 'Vigilance'),
        ('emergency', 'Urgence'),
    ]

    title = models.CharField(max_length=200)
    alert_type = models.CharField(max_length=20, choices=ALERT_TYPES, default='warning')
    message = models.TextField()
    risk_zone = models.ForeignKey(RiskZone, on_delete=models.CASCADE, related_name='alerts', null=True, blank=True)
    
    # Géolocalisation
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    
    # Dates
    issued_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-issued_at']
        indexes = [
            models.Index(fields=['active', '-issued_at']),
        ]

    def __str__(self):
        return f"{self.get_alert_type_display()}: {self.title}"
