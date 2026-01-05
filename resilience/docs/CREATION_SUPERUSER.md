# Documentation : Création du Superutilisateur Django

## Contexte

Cette documentation décrit le processus de création d'un superutilisateur Django pour accéder à l'interface d'administration du projet Resilience Magazine. Le processus a été effectué dans un environnement Docker où l'interaction interactive n'est pas directement possible.

## Problème initial

Lors de la tentative de création d'un superutilisateur avec la commande Django standard `createsuperuser`, nous avons rencontré le problème suivant :

```
Superuser creation skipped due to not running in a TTY.
```

Cela se produit car Docker Compose n'exécute pas les commandes dans un terminal interactif (TTY) par défaut, ce qui empêche la saisie interactive des informations du superutilisateur.

## Solution : Script Python non-interactif

### Étape 1 : Création du script `create_superuser.py`

**Fichier créé** : `/mnt/hackwrld/Projects/resilience/backend/create_superuser.py`

**Raison** : Créer un script Python qui peut créer un superutilisateur de manière non-interactive, en utilisant des variables d'environnement ou des valeurs par défaut.

**Contenu du script** :

- Configuration de Django avec `django.setup()`
- Récupération du modèle User via `get_user_model()`
- Lecture des informations depuis les variables d'environnement avec valeurs par défaut :
  - `DJANGO_SUPERUSER_USERNAME` (défaut: 'admin')
  - `DJANGO_SUPERUSER_EMAIL` (défaut: 'admin@resilience.com')
  - `DJANGO_SUPERUSER_PASSWORD` (défaut: 'admin123')
- Vérification de l'existence de l'utilisateur avant création
- Création du superutilisateur avec `User.objects.create_superuser()`

### Étape 2 : Vérification de l'état des conteneurs Docker

**Commande exécutée** :

```bash
cd /mnt/hackwrld/Projects/resilience/docker && docker compose ps
```

**Raison** : Vérifier que les conteneurs (backend, db, frontend) sont en cours d'exécution avant de procéder.

**Résultat** :

- Conteneur `docker-backend-1` : En cours d'exécution (unhealthy)
- Conteneur `docker-db-1` : En cours d'exécution (healthy)
- Conteneur `docker-frontend-1` : En cours d'exécution

### Étape 3 : Tentative de création interactive (échouée)

**Commande exécutée** :

```bash
cd /mnt/hackwrld/Projects/resilience/docker && docker compose exec backend python manage.py createsuperuser
```

**Raison** : Tentative initiale avec la commande Django standard.

**Résultat** : Échec - "Superuser creation skipped due to not running in a TTY"

**Commande alternative tentée** :

```bash
cd /mnt/hackwrld/Projects/resilience/docker && docker compose exec -it backend python manage.py createsuperuser
```

**Résultat** : Échec - Même erreur, l'option `-it` n'a pas résolu le problème dans ce contexte.

### Étape 4 : Exécution du script (première tentative - échec)

**Commande exécutée** :

```bash
cd /mnt/hackwrld/Projects/resilience/docker && docker compose exec backend python manage.py shell < ../backend/create_superuser.py
```

**Raison** : Exécuter le script via le shell Django.

**Résultat** : Échec avec l'erreur suivante :

```
django.db.utils.ProgrammingError: relation "users_userprofile" does not exist
```

**Explication** : Les migrations des applications personnalisées n'avaient pas été créées ni appliquées. Le modèle `UserProfile` dans `api.users.models` utilise un signal `post_save` qui tente de créer automatiquement un profil lors de la création d'un utilisateur, mais la table n'existait pas encore.

### Étape 5 : Vérification de l'état des migrations

**Commande exécutée** :

```bash
cd /mnt/hackwrld/Projects/resilience/docker && docker compose exec backend python manage.py migrate
```

**Raison** : Vérifier et appliquer les migrations existantes.

**Résultat** : Seules les migrations de base Django étaient appliquées (admin, auth, contenttypes, sessions). Les migrations des applications personnalisées n'existaient pas.

**Commande de vérification** :

```bash
cd /mnt/hackwrld/Projects/resilience/docker && docker compose exec backend python manage.py showmigrations
```

**Résultat** : Confirmation que seules les migrations de base étaient présentes.

### Étape 6 : Création des migrations pour les applications personnalisées

**Commande exécutée** :

```bash
cd /mnt/hackwrld/Projects/resilience/docker && docker compose exec backend python manage.py makemigrations articles users first_aid multimedia library content contact maps
```

**Raison** : Créer les fichiers de migration pour toutes les applications personnalisées du projet qui contiennent des modèles.

**Résultat** : Succès - Migrations créées pour :

- `articles` : Category, Tag, Article
- `contact` : ContactMessage, ReporterApplication
- `content` : Dossier, DossierSection
- `first_aid` : FirstAidGuide, FirstAidVideo, Quiz, Badge, QuizQuestion, QuizAnswer, UserBadge
- `library` : ResourceCategory, Resource
- `maps` : RiskZone, Alert
- `multimedia` : Video, Podcast, Photo, Webinar
- `users` : UserProfile, Comment, SavedContent, NewsletterSubscription

### Étape 7 : Application des migrations

**Commande exécutée** :

```bash
cd /mnt/hackwrld/Projects/resilience/docker && docker compose exec backend python manage.py migrate
```

**Raison** : Appliquer toutes les migrations créées à la base de données PostgreSQL.

**Résultat** : Succès - Toutes les migrations ont été appliquées :

```
Applying articles.0001_initial... OK
Applying contact.0001_initial... OK
Applying content.0001_initial... OK
Applying first_aid.0001_initial... OK
Applying library.0001_initial... OK
Applying maps.0001_initial... OK
Applying multimedia.0001_initial... OK
Applying users.0001_initial... OK
```

### Étape 8 : Création du superutilisateur (succès)

**Commande exécutée** :

```bash
cd /mnt/hackwrld/Projects/resilience/docker && docker compose exec backend python /app/create_superuser.py
```

**Raison** : Exécuter le script Python directement dans le conteneur backend.

**Résultat** :

```
Le superutilisateur 'admin' existe déjà.
```

**Explication** : Le superutilisateur avait probablement été créé lors d'une tentative précédente ou existait déjà dans la base de données.

### Étape 9 : Vérification des superutilisateurs existants

**Commande exécutée** :

```bash
cd /mnt/hackwrld/Projects/resilience/docker && docker compose exec backend python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); superusers = User.objects.filter(is_superuser=True); print('Superutilisateurs existants:'); [print(f'  - {u.username} (email: {u.email})') for u in superusers]"
```

**Raison** : Vérifier quels superutilisateurs existent dans la base de données.

**Résultat** :

```
Superutilisateurs existants:
  - admin (email: admin@resilience.com)
```

## Résultat final

Un superutilisateur Django a été créé avec succès :

- **Nom d'utilisateur** : `admin`
- **Email** : `admin@resilience.com`
- **Mot de passe** : Défini lors de la création (valeur par défaut du script : `admin123` si aucune variable d'environnement n'était définie)

## Accès à l'interface d'administration

L'interface d'administration Django est accessible à :

- **URL** : http://localhost:8888/admin/
- **Identifiants** : Utiliser les informations du superutilisateur créé

## Commandes de référence

### Créer un nouveau superutilisateur avec le script

```bash
cd docker
docker compose exec backend python /app/create_superuser.py
```

### Créer un superutilisateur avec des identifiants personnalisés

Définir les variables d'environnement avant d'exécuter le script :

```bash
cd docker
docker compose exec -e DJANGO_SUPERUSER_USERNAME=monadmin -e DJANGO_SUPERUSER_EMAIL=monemail@example.com -e DJANGO_SUPERUSER_PASSWORD=monmotdepasse backend python /app/create_superuser.py
```

### Réinitialiser le mot de passe d'un superutilisateur existant

```bash
cd docker
docker compose exec backend python manage.py changepassword admin
```

### Vérifier les superutilisateurs existants

```bash
cd docker
docker compose exec backend python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); [print(f'{u.username} - {u.email}') for u in User.objects.filter(is_superuser=True)]"
```

## Notes importantes

1. **Sécurité** : Le script utilise des valeurs par défaut pour le mot de passe (`admin123`). En production, il est fortement recommandé de :

   - Utiliser des variables d'environnement sécurisées
   - Changer le mot de passe immédiatement après la première connexion
   - Utiliser un mot de passe fort

2. **Migrations** : Avant de créer un superutilisateur, assurez-vous que toutes les migrations sont appliquées, notamment celles des applications qui utilisent des signaux Django (comme `UserProfile` dans `api.users.models`).

3. **Script réutilisable** : Le script `create_superuser.py` peut être réutilisé à tout moment pour créer de nouveaux superutilisateurs ou vérifier l'existence d'un utilisateur avant de le créer.

## Fichiers créés/modifiés

- `/mnt/hackwrld/Projects/resilience/backend/create_superuser.py` : Script Python pour création non-interactive du superutilisateur
- Migrations créées dans chaque application Django :
  - `backend/api/articles/migrations/0001_initial.py`
  - `backend/api/users/migrations/0001_initial.py`
  - `backend/api/first_aid/migrations/0001_initial.py`
  - `backend/api/multimedia/migrations/0001_initial.py`
  - `backend/api/library/migrations/0001_initial.py`
  - `backend/api/content/migrations/0001_initial.py`
  - `backend/api/contact/migrations/0001_initial.py`
  - `backend/api/maps/migrations/0001_initial.py`
