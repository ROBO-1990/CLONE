from rest_framework import serializers
from .models import FirstAidGuide, FirstAidVideo, Quiz, QuizQuestion, QuizAnswer, Badge, UserBadge


class FirstAidGuideSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    poster_url = serializers.SerializerMethodField()

    class Meta:
        model = FirstAidGuide
        fields = [
            'id', 'title', 'urgency_type', 'content', 'image_url',
            'poster_url', 'checklist_items', 'created_at', 'updated_at'
        ]

    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None

    def get_poster_url(self, obj):
        if obj.downloadable_poster:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.downloadable_poster.url)
            return obj.downloadable_poster.url
        return None


class FirstAidVideoSerializer(serializers.ModelSerializer):
    thumbnail_url = serializers.SerializerMethodField()

    class Meta:
        model = FirstAidVideo
        fields = [
            'id', 'title', 'description', 'video_url', 'thumbnail_url',
            'duration', 'guide', 'created_at'
        ]

    def get_thumbnail_url(self, obj):
        if obj.thumbnail:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.thumbnail.url)
            return obj.thumbnail.url
        return None


class QuizAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizAnswer
        fields = ['id', 'answer_text', 'order']


class QuizQuestionSerializer(serializers.ModelSerializer):
    answers = QuizAnswerSerializer(many=True, read_only=True)

    class Meta:
        model = QuizQuestion
        fields = ['id', 'question_text', 'answers', 'order']


class QuizSerializer(serializers.ModelSerializer):
    questions = QuizQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'guide', 'questions', 'created_at']


class QuizSubmissionSerializer(serializers.Serializer):
    quiz_id = serializers.IntegerField()
    answers = serializers.DictField(child=serializers.IntegerField())


class BadgeSerializer(serializers.ModelSerializer):
    icon_url = serializers.SerializerMethodField()

    class Meta:
        model = Badge
        fields = [
            'id', 'name', 'description', 'icon_url', 'level',
            'required_score', 'created_at'
        ]

    def get_icon_url(self, obj):
        if obj.icon:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.icon.url)
            return obj.icon.url
        return None


class UserBadgeSerializer(serializers.ModelSerializer):
    badge = BadgeSerializer(read_only=True)

    class Meta:
        model = UserBadge
        fields = ['id', 'badge', 'earned_at', 'quiz_score']
