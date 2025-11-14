from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'full_name', 'role', 'avatar', 'bio']
        read_only_fields = ['role']  # Admins set roles
