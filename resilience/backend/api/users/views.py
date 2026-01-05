from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
from .models import UserProfile, Comment, SavedContent
from .serializers import (
    UserSerializer, UserRegistrationSerializer, UserProfileSerializer,
    CommentSerializer, SavedContentSerializer
)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        return token


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]

    def get_serializer_class(self):
        if self.action == 'create':
            return UserRegistrationSerializer
        return UserSerializer

    @action(detail=False, methods=['get', 'put', 'patch'])
    def me(self, request):
        """Récupère ou met à jour le profil de l'utilisateur connecté"""
        if request.method == 'GET':
            serializer = self.get_serializer(request.user)
            return Response(serializer.data)
        elif request.method in ['PUT', 'PATCH']:
            serializer = self.get_serializer(request.user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def badges(self, request):
        """Retourne les badges de l'utilisateur"""
        from api.first_aid.models import UserBadge
        badges = UserBadge.objects.filter(user=request.user).select_related('badge')
        from api.first_aid.serializers import UserBadgeSerializer
        serializer = UserBadgeSerializer(badges, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get', 'post'])
    def saved_content(self, request):
        """Récupère ou ajoute du contenu sauvegardé"""
        if request.method == 'GET':
            saved = SavedContent.objects.filter(user=request.user)
            serializer = SavedContentSerializer(saved, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = SavedContentSerializer(data={**request.data, 'user': request.user.id})
            serializer.is_valid(raise_exception=True)
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.filter(approved=True)
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        article_id = self.request.query_params.get('article', None)
        if article_id:
            return self.queryset.filter(article_id=article_id)
        return self.queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
