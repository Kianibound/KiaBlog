from rest_framework import serializers
from apps.articles.models import Article


class ArticleListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Article
    fields = ['id', 'title', 'content', 'created_at', 'updated_at']
    
    
class ArticleDetailSerializer(serializers.ModelSerializer):
  class Meta:
    model = Article
    fields = ['id', 'title', 'content', 'created_at', 'updated_at']
    


class ArticleCreateUpdateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Article
    fields = ['title', 'content']