from rest_framework import serializers
from .models import Dossier, DossierSection


class DossierSectionSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = DossierSection
        fields = ['id', 'title', 'content', 'image_url', 'order']

    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None


class DossierSerializer(serializers.ModelSerializer):
    sections = DossierSectionSerializer(many=True, read_only=True)
    author = serializers.StringRelatedField(read_only=True)
    cover_image_url = serializers.SerializerMethodField()

    class Meta:
        model = Dossier
        fields = [
            'id', 'title', 'slug', 'description', 'cover_image_url',
            'sections', 'author', 'featured', 'published',
            'created_at', 'updated_at', 'published_at'
        ]
        read_only_fields = ['created_at', 'updated_at']

    def get_cover_image_url(self, obj):
        if obj.cover_image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.cover_image.url)
            return obj.cover_image.url
        return None


class DossierListSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    cover_image_url = serializers.SerializerMethodField()

    class Meta:
        model = Dossier
        fields = [
            'id', 'title', 'slug', 'description', 'cover_image_url',
            'author', 'featured', 'published_at', 'created_at'
        ]

    def get_cover_image_url(self, obj):
        if obj.cover_image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.cover_image.url)
            return obj.cover_image.url
        return None
