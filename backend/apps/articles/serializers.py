from rest_framework import serializers
from .models import Article
from apps.categories_tags.models import Category, Tag
from apps.categories_tags.serializers import CategorySerializer, TagSerializer
from apps.users.serializers import UserSerializer  # Your new one

class ArticleSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)  # Nested: Shows full user on GET (e.g., username/role)
    category = CategorySerializer(read_only=True)  # Existing nested read
    tags = TagSerializer(many=True, read_only=True)  # Existing

    class Meta:
        model = Article
        fields = ['id', 'title', 'slug', 'content', 'status', 'author', 'category', 'tags', 'created_at', 'updated_at']
        read_only_fields = ['slug', 'created_at', 'updated_at', 'author']  # Add author: No frontend override

    def validate_title(self, value):  # Existing: Custom val
        if len(value) < 5:
            raise serializers.ValidationError("Title too short – make it catchy!")
        return value

    def create(self, validated_data):
        # Merge: Auto-author + pop/handle relations (your tags logic + category)
        validated_data['author'] = self.context['request'].user  # Secure: Ties to logged user
        category_data = validated_data.pop('category', None)  # ID or None (write: simple ID)
        tags_data = validated_data.pop('tags', [])  # List of IDs or dicts (your existing)
        
        article = Article.objects.create(**validated_data)  # Core create
        
        # Handle category (FK: Set if provided)
        if category_data:
            category, _ = Category.objects.get_or_create(id=category_data)  # Assume ID; adjust if dict
            article.category = category
            article.save()  # Quick update (perf: Batch in prod)
        
        # Your tags logic: Add M2M
        for tag_data in tags_data:
            if isinstance(tag_data, int):  # ID mode (simple)
                tag = Tag.objects.get(id=tag_data)
            else:  # Dict mode (name-based, your original)
                tag, _ = Tag.objects.get_or_create(**tag_data)
            article.tags.add(tag)
        
        return article

    def update(self, instance, validated_data):
        # Symmetric: Pop relations, update core, re-set
        category_data = validated_data.pop('category', None)
        tags_data = validated_data.pop('tags', None)
        
        instance = super().update(instance, validated_data)  # Core fields
        
        if category_data is not None:
            category, _ = Category.objects.get_or_create(id=category_data)
            instance.category = category
            instance.save()
        
        if tags_data is not None:
            instance.tags.set(tags_data)  # Bulk set (faster than loop; DRF optimizes)
        
        return instance