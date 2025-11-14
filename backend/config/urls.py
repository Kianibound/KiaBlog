
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # versioning – /api/v1/articles/
    path('api/v1/', include('apps.articles.urls')),
    # versioning – /api/v1/categories/
    path('api/v1/', include('apps.categories_tags.urls')),
    # versioning – /api/v1/comments/
    path('api/v1/', include('apps.comments.urls')),
]
