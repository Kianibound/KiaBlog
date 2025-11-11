from django.apps import AppConfig

class ArticlesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Modern PK (Django 3.2+)
    name = 'apps.articles'
    verbose_name = 'Articles App'