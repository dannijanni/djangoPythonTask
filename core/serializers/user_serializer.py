# core/serializers/users.py

from rest_framework import serializers
from core.models import Users
from core.security import hash_password

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'full_name', 'email', 'password_hash', 'role']

    def create(self, validated_data):
        validated_data['password_hash'] = hash_password(validated_data['password_hash'])
        return super().create(validated_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'full_name', 'email', 'role', 'created_at', 'updated_at']
