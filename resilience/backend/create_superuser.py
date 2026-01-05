#!/usr/bin/env python
"""Script pour créer un superutilisateur Django de manière non-interactive"""
import os
import django

# Configuration de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'resilience.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Informations du superutilisateur
username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'admin')
email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'admin@resilience.com')
password = os.getenv('DJANGO_SUPERUSER_PASSWORD', 'admin123')

# Vérifier si l'utilisateur existe déjà
if User.objects.filter(username=username).exists():
    print(f"Le superutilisateur '{username}' existe déjà.")
else:
    # Créer le superutilisateur
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"Superutilisateur '{username}' créé avec succès!")
    print(f"Email: {email}")
    print(f"Mot de passe: {password}")

