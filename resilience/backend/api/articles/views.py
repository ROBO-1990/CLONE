from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Article, Category, Tag
from .serializers import ArticleSerializer, ArticleListSerializer, CategorySerializer, TagSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'slug'


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.filter(published=True).select_related('category', 'author').prefetch_related('tags')
    serializer_class = ArticleListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['article_type', 'category', 'tags', 'featured']
    search_fields = ['title', 'content', 'excerpt']
    ordering_fields = ['created_at', 'published_at', 'title']
    ordering = ['-published_at', '-created_at']
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ArticleSerializer
        return ArticleListSerializer

    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Retourne les articles mis en vedette"""
        featured_articles = self.queryset.filter(featured=True)[:5]
        serializer = self.get_serializer(featured_articles, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def latest(self, request):
        """Retourne les derniers articles"""
        latest_articles = self.queryset[:10]
        serializer = self.get_serializer(latest_articles, many=True)
        return Response(serializer.data)
