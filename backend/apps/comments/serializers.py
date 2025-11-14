from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    article_title = serializers.CharField(
        source='article.title', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'article', 'article_title', 'author_name',
                  'author_email', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['article', 'author_name', 'author_email', 'content']

    def validate_content(self, value):
        if len(value.strip()) < 5:
            raise serializers.ValidationError(
                "Content must be at least 5 characters long.")
        return value
