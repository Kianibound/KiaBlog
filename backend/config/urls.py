
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # Your versioning – /api/v1/articles/
    path('api/v1/', include('apps.articles.urls')),
]
