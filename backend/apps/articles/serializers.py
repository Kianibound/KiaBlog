from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'slug', 'content',
                  'status', 'created_at', 'updated_at']
        # Prevent tampering – security best
        read_only_fields = ['slug', 'created_at', 'updated_at']

    def validate_title(self, value):  # Custom validation: Real-world edge case
        if len(value) < 5:
            raise serializers.ValidationError(
                "Title too short – make it catchy!")
        return value
