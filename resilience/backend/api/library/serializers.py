from rest_framework import serializers
from .models import Resource, ResourceCategory


class ResourceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceCategory
        fields = ['id', 'name', 'slug', 'description']


class ResourceSerializer(serializers.ModelSerializer):
    category = ResourceCategorySerializer(read_only=True)
    file_url = serializers.SerializerMethodField()
    thumbnail_url = serializers.SerializerMethodField()

    class Meta:
        model = Resource
        fields = [
            'id', 'title', 'description', 'resource_type', 'category',
            'file_url', 'thumbnail_url', 'author', 'organization',
            'publication_date', 'language', 'download_count',
            'published', 'created_at', 'updated_at'
        ]
        read_only_fields = ['download_count', 'created_at', 'updated_at']

    def get_file_url(self, obj):
        if obj.file:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.file.url)
            return obj.file.url
        return None

    def get_thumbnail_url(self, obj):
        if obj.thumbnail:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.thumbnail.url)
            return obj.thumbnail.url
        return None


class ResourceListSerializer(serializers.ModelSerializer):
    category = ResourceCategorySerializer(read_only=True)
    thumbnail_url = serializers.SerializerMethodField()

    class Meta:
        model = Resource
        fields = [
            'id', 'title', 'description', 'resource_type', 'category',
            'thumbnail_url', 'author', 'organization', 'publication_date',
            'language', 'download_count', 'published', 'created_at'
        ]

    def get_thumbnail_url(self, obj):
        if obj.thumbnail:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.thumbnail.url)
            return obj.thumbnail.url
        return None
