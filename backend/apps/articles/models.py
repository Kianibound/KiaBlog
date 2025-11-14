from django.db import models
from django.utils.text import slugify
from apps.core.models import TimeStampedModel
from apps.categories_tags.models import Category, Tag
from apps.users.models import User


class ArticleStatus(models.TextChoices):
    DRAFT = 'draft', 'Draft'
    PUBLISHED = 'published', 'Published'


class Article(TimeStampedModel):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='articles')  # Writer owns
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = models.TextField()
    status = models.CharField(
        max_length=10, choices=ArticleStatus.choices, default=ArticleStatus.DRAFT)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='articles')
    tags = models.ManyToManyField(Tag, blank=True, related_name='articles')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Articles'
