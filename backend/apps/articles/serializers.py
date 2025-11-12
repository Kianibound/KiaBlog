from rest_framework import serializers
from .models import Article
from apps.categories_tags.models import Tag
from apps.categories_tags.serializers import CategorySerializer, TagSerializer


class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'slug', 'content', 'status',
                  'category', 'tags', 'created_at', 'updated_at']
        read_only_fields = ['slug', 'created_at', 'updated_at']

    def create(self, validated_data):
        """
        Create an Article instance with the given validated data.
        If 'tags' is present in the validated data, create or get the
        corresponding Tag instances and add them to the Article instance.
        """
        tags_data = validated_data.pop('tags', [])
        article = Article.objects.create(**validated_data)
        for tag_data in tags_data:
            tag, _ = Tag.objects.get_or_create(**tag_data)
            article.tags.add(tag)
        return article

    def update(self, instance, validated_data):
        """
        Update an Article instance with the given validated data.
        If 'tags' is present in the validated data, replace the
        Article instance's tags with the given tags.
        """
        tags_data = validated_data.pop('tags', None)
        if tags_data is not None:
            instance.tags.set(tags_data)
        return super().update(instance, validated_data)
