# Resilience Magazine

Site web pour Resilience Magazine - Gouvernance des risques et résilience.

## Architecture

- **Backend**: Django 5.2.9 + Django REST Framework
- **Frontend**: React 18.2.0
- **Base de données**: PostgreSQL 18
- **Containerisation**: Docker & Docker Compose

## Structure du Projet

```
resilience/
├── docker/                 # Configuration Docker
│   ├── backend/
│   │   └── Dockerfile
│   ├── frontend/
│   │   └── Dockerfile
│   └── docker-compose.yml
├── backend/                 # Django project
│   ├── api/                # Apps Django REST API
│   ├── resilience/         # Settings Django
│   └── requirements.txt
├── frontend/               # React SPA
│   ├── src/
│   └── package.json
└── .env                    # Variables d'environnement
```

## Installation

### Prérequis

- Docker 20.10+
- Docker Compose 2.0+

### Configuration

1. Copiez le fichier `.env.example` vers `.env` et configurez les variables :

```bash
cp .env.example .env
```

2. Modifiez les variables dans `.env` selon vos besoins.

### Démarrage

Lancez tous les services avec Docker Compose :

```bash
cd docker
docker compose up -d
```

Cela démarre :

- PostgreSQL sur le port 5432
- Django API sur le port 8888 (mappé depuis le port 8000 interne)
- React frontend sur le port 3000

### Accès

- Frontend: http://localhost:3000
- Backend API: http://localhost:8888/api/
- Django Admin: http://localhost:8888/admin/
- API Documentation: http://localhost:8888/api/docs/

## Développement

### Backend

Pour travailler sur le backend :

```bash
cd backend
source venv/bin/activate  # Si vous utilisez un venv local
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Frontend

Pour travailler sur le frontend :

```bash
cd frontend
npm install
npm start
```

## API Endpoints

### Articles

- `GET /api/articles/` - Liste des articles
- `GET /api/articles/{slug}/` - Détail d'un article
- `GET /api/articles/featured/` - Articles en vedette
- `GET /api/articles/latest/` - Derniers articles

### Premiers Secours

- `GET /api/first-aid/guides/` - Guides de premiers secours
- `GET /api/first-aid/videos/` - Vidéos tutoriels
- `GET /api/first-aid/quiz/` - Quiz disponibles
- `POST /api/first-aid/quiz/{id}/submit/` - Soumettre un quiz

### Multimédia

- `GET /api/multimedia/videos/` - Vidéos
- `GET /api/multimedia/podcasts/` - Podcasts
- `GET /api/multimedia/photos/` - Photos
- `GET /api/multimedia/webinars/` - Webinaires

### Bibliothèque

- `GET /api/library/resources/` - Ressources
- `GET /api/library/resources/{id}/download/` - Télécharger une ressource

### Utilisateurs & Authentification

- `POST /api/users/auth/register/` - Inscription
- `POST /api/users/auth/login/` - Connexion
- `GET /api/users/me/` - Profil utilisateur
- `GET /api/users/me/badges/` - Badges de l'utilisateur

### Recherche

- `GET /api/search/?q=query` - Recherche globale

## Documentation API

La documentation Swagger/OpenAPI est disponible à :
http://localhost:8888/api/docs/

## Notes

- Les médias uploadés sont stockés dans `backend/media/`
- Les fichiers statiques sont collectés dans `backend/staticfiles/`
- La base de données PostgreSQL est persistée dans un volume Docker
