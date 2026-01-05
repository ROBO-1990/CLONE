from django.db import models


class ContactMessage(models.Model):
    """Messages de contact"""
    SUBJECT_TYPES = [
        ('general', 'Question générale'),
        ('editorial', 'Rédaction'),
        ('partnership', 'Partenariat'),
        ('report', 'Signaler un problème'),
        ('other', 'Autre'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject_type = models.CharField(max_length=20, choices=SUBJECT_TYPES, default='general')
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    replied = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.subject} - {self.name}"


class ReporterApplication(models.Model):
    """Formulaire 'Reporters du monde'"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=200)
    motivation = models.TextField()
    experience = models.TextField(blank=True)
    cv_file = models.FileField(upload_to='contact/reporters/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    reviewed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Application from {self.name} - {self.location}"
