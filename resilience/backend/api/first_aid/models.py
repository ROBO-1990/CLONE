from django.db import models
from django.contrib.auth.models import User


class FirstAidGuide(models.Model):
    """Guides de premiers secours par type d'urgence"""
    URGENCY_TYPES = [
        ('flood', 'Inondation'),
        ('earthquake', 'Séisme'),
        ('fire', 'Incendie'),
        ('landslide', 'Glissement de terrain'),
        ('storm', 'Tempête / Vents violents'),
        ('heatwave', 'Canicule'),
    ]

    title = models.CharField(max_length=200)
    urgency_type = models.CharField(max_length=20, choices=URGENCY_TYPES)
    content = models.TextField()
    image = models.ImageField(upload_to='first_aid/guides/', blank=True, null=True)
    downloadable_poster = models.FileField(upload_to='first_aid/posters/', blank=True, null=True)
    
    # Checklist
    checklist_items = models.JSONField(default=list, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['urgency_type', 'title']

    def __str__(self):
        return f"{self.get_urgency_type_display()} - {self.title}"


class FirstAidVideo(models.Model):
    """Vidéos tutoriels de premiers secours"""
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    video_url = models.URLField()
    thumbnail = models.ImageField(upload_to='first_aid/videos/', blank=True, null=True)
    duration = models.PositiveIntegerField(help_text="Durée en secondes", null=True, blank=True)
    
    # Relation avec guide
    guide = models.ForeignKey(FirstAidGuide, on_delete=models.SET_NULL, null=True, blank=True, related_name='videos')
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Quiz(models.Model):
    """Quiz d'évaluation pour premiers secours"""
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    guide = models.ForeignKey(FirstAidGuide, on_delete=models.SET_NULL, null=True, blank=True, related_name='quizzes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Quizzes"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class QuizQuestion(models.Model):
    """Questions d'un quiz"""
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f"{self.quiz.title} - Question {self.order}"


class QuizAnswer(models.Model):
    """Réponses possibles pour une question"""
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE, related_name='answers')
    answer_text = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f"{self.question} - {self.answer_text}"


class Badge(models.Model):
    """Badges de certification"""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    icon = models.ImageField(upload_to='badges/', blank=True, null=True)
    level = models.PositiveIntegerField(default=1, help_text="Niveau du badge (1, 2, 3...)")
    quiz = models.ForeignKey(Quiz, on_delete=models.SET_NULL, null=True, blank=True, related_name='badges')
    required_score = models.PositiveIntegerField(default=80, help_text="Score minimum requis (%)")
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['level', 'name']

    def __str__(self):
        return f"{self.name} (Niveau {self.level})"


class UserBadge(models.Model):
    """Attribution de badges aux utilisateurs"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='badges')
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE, related_name='user_badges')
    earned_at = models.DateTimeField(auto_now_add=True)
    quiz_score = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        unique_together = ['user', 'badge']
        ordering = ['-earned_at']

    def __str__(self):
        return f"{self.user.username} - {self.badge.name}"
