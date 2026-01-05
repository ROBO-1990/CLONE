from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .models import FirstAidGuide, FirstAidVideo, Quiz, QuizQuestion, QuizAnswer, Badge, UserBadge
from .serializers import (
    FirstAidGuideSerializer, FirstAidVideoSerializer, QuizSerializer,
    QuizSubmissionSerializer, BadgeSerializer, UserBadgeSerializer
)


class FirstAidGuideViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FirstAidGuide.objects.all()
    serializer_class = FirstAidGuideSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['urgency_type']


class FirstAidVideoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FirstAidVideo.objects.all()
    serializer_class = FirstAidVideoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['guide']


class QuizViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['guide']

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def submit(self, request, pk=None):
        """Soumet les réponses d'un quiz et attribue un badge si le score est suffisant"""
        quiz = self.get_object()
        answers = request.data.get('answers', {})
        
        questions = quiz.questions.all()
        correct_count = 0
        total_questions = questions.count()
        
        for question in questions:
            answer_id = answers.get(str(question.id))
            if answer_id:
                answer = QuizAnswer.objects.filter(id=answer_id, question=question).first()
                if answer and answer.is_correct:
                    correct_count += 1
        
        score = int((correct_count / total_questions) * 100) if total_questions > 0 else 0
        
        # Vérifier si un badge peut être attribué
        badges_earned = []
        if score >= 80:  # Score minimum pour un badge
            badge = Badge.objects.filter(quiz=quiz, required_score__lte=score).first()
            if badge:
                user_badge, created = UserBadge.objects.get_or_create(
                    user=request.user,
                    badge=badge,
                    defaults={'quiz_score': score}
                )
                if created:
                    badges_earned.append(BadgeSerializer(badge).data)
        
        return Response({
            'score': score,
            'correct_answers': correct_count,
            'total_questions': total_questions,
            'badges_earned': badges_earned
        })


class BadgeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer
