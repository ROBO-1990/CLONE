from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import ContactMessage, ReporterApplication
from api.users.models import NewsletterSubscription
from .serializers import (
    ContactMessageSerializer, ReporterApplicationSerializer,
    NewsletterSubscriptionSerializer
)


class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {'message': 'Votre message a été envoyé avec succès.'},
            status=status.HTTP_201_CREATED,
            headers=headers
        )


class ReporterApplicationViewSet(viewsets.ModelViewSet):
    queryset = ReporterApplication.objects.all()
    serializer_class = ReporterApplicationSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {'message': 'Votre candidature a été reçue avec succès.'},
            status=status.HTTP_201_CREATED,
            headers=headers
        )


class NewsletterViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'])
    def subscribe(self, request):
        """Abonnement à la newsletter"""
        email = request.data.get('email')
        name = request.data.get('name', '')
        
        if not email:
            return Response(
                {'error': 'Email requis'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        subscription, created = NewsletterSubscription.objects.get_or_create(
            email=email,
            defaults={'name': name, 'active': True}
        )
        
        if not created and not subscription.active:
            subscription.active = True
            subscription.save()
        
        return Response(
            {'message': 'Abonnement réussi à la newsletter.'},
            status=status.HTTP_201_CREATED
        )
