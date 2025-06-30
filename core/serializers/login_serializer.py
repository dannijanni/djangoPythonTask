# core/serializers/login_serializer.py
from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    user_type = serializers.CharField()