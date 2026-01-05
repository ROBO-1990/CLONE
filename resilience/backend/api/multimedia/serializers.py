from rest_framework import serializers
from .models import Video, Podcast, Photo, Webinar


class VideoSerializer(serializers.ModelSerializer):
    thumbnail_url = serializers.SerializerMethodField()
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Video
        fields = [
            'id', 'title', 'description', 'video_url', 'thumbnail_url',
            'video_type', 'duration', 'author', 'published', 'created_at'
        ]

    def get_thumbnail_url(self, obj):
        if obj.thumbnail:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.thumbnail.url)
            return obj.thumbnail.url
        return None


class PodcastSerializer(serializers.ModelSerializer):
    thumbnail_url = serializers.SerializerMethodField()
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Podcast
        fields = [
            'id', 'title', 'description', 'audio_url', 'thumbnail_url',
            'duration', 'episode_number', 'author', 'published', 'created_at'
        ]

    def get_thumbnail_url(self, obj):
        if obj.thumbnail:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.thumbnail.url)
            return obj.thumbnail.url
        return None


class PhotoSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Photo
        fields = [
            'id', 'title', 'description', 'image_url', 'gallery_name',
            'author', 'published', 'created_at'
        ]

    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None


class WebinarSerializer(serializers.ModelSerializer):
    thumbnail_url = serializers.SerializerMethodField()

    class Meta:
        model = Webinar
        fields = [
            'id', 'title', 'description', 'video_url', 'thumbnail_url',
            'scheduled_at', 'duration', 'speaker', 'published', 'created_at'
        ]

    def get_thumbnail_url(self, obj):
        if obj.thumbnail:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.thumbnail.url)
            return obj.thumbnail.url
        return None
