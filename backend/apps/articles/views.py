from django.shortcuts import render
from rest_framework import viewsets
from apps.articles.models import Article
from apps.articles.serializers import ArticleListSerializer


class ArticleViewSet(viewsets.ModelViewSet):
  queryset = Article.objects.all()
  serializer_class = ArticleListSerializer
