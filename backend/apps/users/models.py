from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.core.models import TimeStampedModel  # Reuse timestamps (DRY win)

class UserRole(models.TextChoices):
    SUPERADMIN = 'superadmin', 'Superadmin'
    ADMIN = 'admin', 'Admin'
    WRITER = 'writer', 'Writer'
    NORMAL = 'normal', 'Normal User'

class User(TimeStampedModel, AbstractUser):  # Concrete: Full table + auth features
    role = models.CharField(max_length=20, choices=UserRole.choices, default=UserRole.NORMAL)
    full_name = models.CharField(max_length=100, blank=True)  # Writer feature
    avatar = models.ImageField(upload_to='avatars/', blank=True)  # Future: Media handling
    bio = models.TextField(blank=True)  # Writer short bio

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-created_at']