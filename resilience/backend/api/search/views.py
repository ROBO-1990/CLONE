from rest_framework import views
from rest_framework.response import Response
from django.db.models import Q
from api.articles.models import Article
from api.content.models import Dossier
from api.multimedia.models import Video, Podcast
from api.library.models import Resource


class SearchView(views.APIView):
    """Recherche globale dans tous les contenus"""
    
    def get(self, request):
        query = request.query_params.get('q', '').strip()
        
        if not query:
            return Response({
                'articles': [],
                'dossiers': [],
                'videos': [],
                'podcasts': [],
                'resources': [],
                'total': 0
            })
        
        # Recherche dans les articles
        articles = Article.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query) | Q(excerpt__icontains=query),
            published=True
        )[:10]
        
        # Recherche dans les dossiers
        dossiers = Dossier.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query),
            published=True
        )[:10]
        
        # Recherche dans les vidéos
        videos = Video.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query),
            published=True
        )[:10]
        
        # Recherche dans les podcasts
        podcasts = Podcast.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query),
            published=True
        )[:10]
        
        # Recherche dans les ressources
        resources = Resource.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query),
            published=True
        )[:10]
        
        # Sérialisation simple
        from api.articles.serializers import ArticleListSerializer
        from api.content.serializers import DossierListSerializer
        from api.multimedia.serializers import VideoSerializer, PodcastSerializer
        from api.library.serializers import ResourceListSerializer
        
        return Response({
            'query': query,
            'articles': ArticleListSerializer(articles, many=True, context={'request': request}).data,
            'dossiers': DossierListSerializer(dossiers, many=True, context={'request': request}).data,
            'videos': VideoSerializer(videos, many=True, context={'request': request}).data,
            'podcasts': PodcastSerializer(podcasts, many=True, context={'request': request}).data,
            'resources': ResourceListSerializer(resources, many=True, context={'request': request}).data,
            'total': articles.count() + dossiers.count() + videos.count() + podcasts.count() + resources.count()
        })

