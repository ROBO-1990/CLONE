---
name: Architecture Resilience Magazine
overview: Création d'une architecture Django REST API + React SPA pour le site Resilience Magazine avec gestion complète de contenu, médias, utilisateurs et fonctionnalités interactives.
todos:
  - id: setup-project-structure
    content: Créer la structure de base du projet (backend Django + frontend React) avec configuration initiale
    status: in_progress
  - id: setup-database-models
    content: Créer les modèles Django pour articles, dossiers, premiers secours, multimédias, bibliothèque, utilisateurs
    status: pending
    dependencies:
      - setup-project-structure
  - id: setup-django-admin
    content: Configurer Django Admin avec interfaces personnalisées pour la gestion de contenu (articles, médias, ressources)
    status: pending
    dependencies:
      - setup-database-models
  - id: implement-api-endpoints
    content: Implémenter les endpoints REST API principaux (articles, dossiers, premiers secours, multimédias, bibliothèque, recherche)
    status: pending
    dependencies:
      - setup-database-models
  - id: implement-authentication
    content: Mettre en place l'authentification JWT et la gestion des utilisateurs (inscription, connexion, profil, badges)
    status: pending
    dependencies:
      - setup-database-models
  - id: setup-react-frontend
    content: Créer la structure React avec routing, composants de base, et intégration avec les services API
    status: pending
    dependencies:
      - implement-api-endpoints
  - id: implement-frontend-pages
    content: Développer les pages principales (accueil, articles, premiers secours, bibliothèque, à propos, contact)
    status: pending
    dependencies:
      - setup-react-frontend
  - id: implement-interactive-features
    content: Implémenter les fonctionnalités interactives (cartes de risques, quiz e-learning, recherche, commentaires)
    status: pending
    dependencies:
      - implement-frontend-pages
  - id: implement-media-management
    content: Configurer la gestion des médias (upload, stockage, affichage de vidéos, podcasts, photos, PDFs)
    status: pending
    dependencies:
      - setup-database-models
  - id: setup-docker-config
    content: Créer la configuration Docker complète (dossier docker/ avec Dockerfiles pour backend/frontend et docker-compose.yml pour PostgreSQL, Django, React)
    status: pending
    dependencies:
      - setup-project-structure
---

# Plan d

'Architecture - Resilience Magazine

## Analyse des Besoins

D'après le PRD, **un backend Django est absolument nécessaire** pour les fonctionnalités suivantes :

### Fonctionnalités nécessitant un backend :

1. **Gestion de contenu** : Articles, actualités, dossiers thématiques, ressources
2. **Médias** : Upload/gestion de vidéos, podcasts, photos, PDFs téléchargeables
3. **Formulaires** : Contact, newsletter, formulaire "Reporters du monde"
4. **Utilisateurs** : Système de badges/certifications, sauvegarde de dossiers, commentaires
5. **Recherche** : Moteur de recherche pour articles et contenus
6. **Alertes** : Système de notifications en temps réel (optionnel)
7. **E-learning** : Modules d'apprentissage, quiz, badges numériques
8. **Bibliothèque** : Gestion et téléchargement de ressources (rapports, guides, outils)
9. **Cartes interactives** : Données géographiques et risques
10. **Multimédia** : Gestion de podcasts, webinaires, reportages photos

## Architecture Technique

### Backend (Django)

- **Framework** : Django 4.x avec Django REST Framework
- **Base de données** : PostgreSQL (recommandé pour le contenu riche)
- **Authentification** : Django REST Framework Simple JWT
- **Médias** : Django FileField/ImageField avec stockage configurable (local/S3)
- **Admin** : Django Admin personnalisé pour la gestion de contenu
- **API** : RESTful API avec documentation Swagger/OpenAPI

### Frontend (React)

- **Framework** : React 18+ avec TypeScript
- **Routing** : React Router v6
- **State Management** : Context API ou Zustand (selon complexité)
- **HTTP Client** : Axios ou Fetch API
- **UI Components** : Bibliothèque moderne (Material-UI, Chakra UI, ou Tailwind CSS)
- **Cartes** : Leaflet ou Mapbox pour les cartes interactives
- **Build** : Vite ou Create React App

### Structure du Projet

```javascript
resilience/
├── docker/                 # Configuration Docker
│   ├── backend/
│   │   └── Dockerfile      # Dockerfile pour Django
│   ├── frontend/
│   │   └── Dockerfile      # Dockerfile pour React
│   └── docker-compose.yml  # Configuration multi-conteneurs
├── backend/                 # Django project
│   ├── resilience/         # Main project settings
│   ├── api/                # Django REST API
│   │   ├── articles/       # App articles/actualités
│   │   ├── content/        # App dossiers, gouvernance, climat
│   │   ├── multimedia/     # App vidéos, podcasts, photos
│   │   ├── first_aid/      # App premiers secours, e-learning
│   │   ├── library/        # App bibliothèque et ressources
│   │   ├── users/          # App utilisateurs, badges
│   │   ├── contact/         # App formulaires de contact
│   │   └── maps/           # App cartes interactives
│   ├── requirements.txt    # Dépendances Python
│   ├── manage.py
│   ├── media/              # Fichiers uploadés (volume Docker)
│   └── static/            # Fichiers statiques (volume Docker)
├── frontend/               # React SPA
│   ├── src/
│   │   ├── components/     # Composants réutilisables
│   │   ├── pages/          # Pages principales
│   │   ├── services/       # API calls
│   │   ├── hooks/          # Custom hooks
│   │   └── utils/          # Utilitaires
│   ├── package.json
│   └── public/
├── .env                    # Variables d'environnement (non versionné)
├── .env.example            # Exemple de configuration
└── docs/                   # Documentation existante
```



## Modèles de Données Principaux

### Articles & Contenu

- `Article` : Articles, actualités, éditos, décryptages
- `Dossier` : Dossiers thématiques avec sections
- `Category` : Catégories (international, national, climat, etc.)
- `Tag` : Tags pour organisation

### Premiers Secours

- `FirstAidGuide` : Guides de premiers secours par type d'urgence
- `FirstAidVideo` : Vidéos tutoriels
- `Quiz` : Quiz d'évaluation
- `Badge` : Badges de certification
- `UserBadge` : Attribution de badges aux utilisateurs

### Multimédia

- `Video` : Vidéos pédagogiques, reportages
- `Podcast` : Épisodes de podcasts
- `Photo` : Galeries photos
- `Webinar` : Webinaires et conférences

### Bibliothèque

- `Resource` : Rapports, guides, outils téléchargeables
- `ResourceCategory` : Catégories de ressources

### Utilisateurs & Communauté

- `User` : Utilisateurs étendus (Django User)
- `Comment` : Commentaires sur articles
- `SavedContent` : Contenus sauvegardés par utilisateurs
- `NewsletterSubscription` : Abonnements newsletter

### Cartes & Données

- `RiskZone` : Zones à risques géographiques
- `Alert` : Alertes en temps réel (optionnel)

## API Endpoints Principaux

### Articles & Contenu

- `GET /api/articles/` : Liste des articles avec filtres
- `GET /api/articles/{id}/` : Détail d'un article
- `GET /api/dossiers/` : Liste des dossiers
- `GET /api/dossiers/{id}/` : Détail d'un dossier

### Premiers Secours

- `GET /api/first-aid/guides/` : Guides par type d'urgence
- `GET /api/first-aid/videos/` : Vidéos tutoriels
- `GET /api/first-aid/quiz/` : Quiz disponibles
- `POST /api/first-aid/quiz/{id}/submit/` : Soumission de quiz
- `GET /api/users/me/badges/` : Badges de l'utilisateur

### Multimédia

- `GET /api/multimedia/videos/` : Liste des vidéos
- `GET /api/multimedia/podcasts/` : Liste des podcasts
- `GET /api/multimedia/photos/` : Galeries photos

### Bibliothèque

- `GET /api/library/resources/` : Ressources disponibles
- `GET /api/library/resources/{id}/download/` : Téléchargement

### Recherche

- `GET /api/search/?q=query` : Recherche globale

### Utilisateurs

- `POST /api/auth/register/` : Inscription
- `POST /api/auth/login/` : Connexion
- `GET /api/users/me/` : Profil utilisateur
- `POST /api/users/me/saved-content/` : Sauvegarder un contenu

### Contact

- `POST /api/contact/` : Formulaire de contact
- `POST /api/newsletter/subscribe/` : Abonnement newsletter

## Architecture Docker

### Structure Docker

```javascript
docker/
├── backend/
│   └── Dockerfile          # Image Django avec Python 3.11
├── frontend/
│   └── Dockerfile          # Image React avec Node 18+
└── docker-compose.yml      # Orchestration des services
```



### Services Docker Compose

1. **db** (PostgreSQL)

- Image : `postgres:14-alpine`
- Port : 5432 (interne uniquement)
- Volume : Persistance des données
- Variables : DB_NAME, DB_USER, DB_PASSWORD depuis `.env`

2. **backend** (Django)

- Build : `docker/backend/Dockerfile`
- Port : 8000 (exposé sur 8000)
- Dépendances : db
- Volumes : Code source, media, static
- Commandes : migrations, collectstatic, runserver

3. **frontend** (React)

- Build : `docker/frontend/Dockerfile`
- Port : 3000 (développement) ou 80 (production)
- Volumes : Code source pour hot-reload en développement
- Proxy : API calls vers backend

### Volumes Docker

- `postgres_data` : Données PostgreSQL (persistance)
- `backend_media` : Fichiers uploadés (médias)
- `backend_static` : Fichiers statiques collectés
- Code source monté en volume pour développement

### Réseau Docker

- Réseau interne `resilience_network` pour communication entre services
- Backend communique avec PostgreSQL via nom de service `db`
- Frontend communique avec Backend via nom de service `backend`

## Configuration & Déploiement

### Variables d'environnement (.env)

- `SECRET_KEY` : Clé secrète Django
- `DEBUG` : Mode debug
- `DATABASE_URL` : URL de connexion PostgreSQL
- `ALLOWED_HOSTS` : Hôtes autorisés
- `MEDIA_ROOT` : Chemin des médias
- `STATIC_ROOT` : Chemin des fichiers statiques
- `CORS_ALLOWED_ORIGINS` : Origines autorisées pour CORS
- `JWT_SECRET_KEY` : Clé pour JWT

### Docker (Architecture Containerisée)

L'application sera entièrement containerisée pour l'isolation et la portabilité :

- **Dossier `docker/`** : Contient toute la configuration Docker
- `docker/backend/Dockerfile` : Image Django avec toutes les dépendances
- `docker/frontend/Dockerfile` : Image React pour build et serveur de développement
- `docker/docker-compose.yml` : Orchestration des services
- **Services Docker** :
- `db` : Conteneur PostgreSQL (base de données isolée)
- `backend` : Conteneur Django (API REST)
- `frontend` : Conteneur React (SPA)
- `nginx` (optionnel) : Reverse proxy pour production
- **Volumes Docker** :
- Volume pour les médias uploadés (persistance)
- Volume pour les fichiers statiques
- Volume pour la base de données PostgreSQL (persistance)
- **Réseau Docker** : Réseau interne pour communication entre services
- **Configuration** : Variables d'environnement via `.env` partagé entre conteneurs

## Étapes d'Implémentation

1. **Setup initial** : Structure Django + React, configuration de base
2. **Modèles de données** : Création des modèles principaux
3. **Django Admin** : Configuration de l'admin pour gestion de contenu
4. **API REST** : Implémentation des endpoints principaux
5. **Authentification** : Système JWT et gestion utilisateurs
6. **Frontend React** : Structure de base, routing, composants UI
7. **Intégration API** : Connexion frontend-backend
8. **Fonctionnalités avancées** : Recherche, cartes, e-learning
9. **Tests** : Tests unitaires et d'intégration
10. **Déploiement** : Configuration pour production

## Technologies Recommandées

### Backend

- Django 4.x
- Django REST Framework 3.14+
- django-cors-headers (pour CORS)
- djangorestframework-simplejwt (authentification)
- Pillow (gestion d'images)
- psycopg2-binary (PostgreSQL)

### Frontend

- React 18+
- TypeScript
- React Router v6
- Axios
- Leaflet (cartes)
- Tailwind CSS ou Material-UI

### Base de données

- PostgreSQL 14+

### Docker & Containerisation

- Docker 20.10+
- Docker Compose 2.0+
- Images de base : Python 3.11 (backend), Node 18+ (frontend), PostgreSQL 14+ (base de données)