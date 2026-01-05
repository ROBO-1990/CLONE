from rest_framework import serializers
from .models import RiskZone, Alert


class RiskZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskZone
        fields = [
            'id', 'name', 'risk_type', 'risk_level', 'description',
            'latitude', 'longitude', 'area_coordinates',
            'preventive_actions', 'emergency_contacts',
            'active', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']


class AlertSerializer(serializers.ModelSerializer):
    risk_zone = RiskZoneSerializer(read_only=True)

    class Meta:
        model = Alert
        fields = [
            'id', 'title', 'alert_type', 'message', 'risk_zone',
            'latitude', 'longitude', 'issued_at', 'expires_at', 'active'
        ]
        read_only_fields = ['issued_at']
