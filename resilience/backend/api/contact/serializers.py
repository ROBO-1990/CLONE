from rest_framework import serializers
from .models import ContactMessage, ReporterApplication


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id', 'name', 'email', 'subject_type', 'subject', 'message', 'created_at']
        read_only_fields = ['created_at']


class ReporterApplicationSerializer(serializers.ModelSerializer):
    cv_file_url = serializers.SerializerMethodField()

    class Meta:
        model = ReporterApplication
        fields = [
            'id', 'name', 'email', 'phone', 'location',
            'motivation', 'experience', 'cv_file_url', 'created_at'
        ]
        read_only_fields = ['created_at']

    def get_cv_file_url(self, obj):
        if obj.cv_file:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.cv_file.url)
            return obj.cv_file.url
        return None


class NewsletterSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReporterApplication  # Utiliser le modèle existant temporairement
        fields = ['email', 'name']
