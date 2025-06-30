# core/schemas/auth.py

from rest_framework import serializers

class LoginRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class LoginResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    email = serializers.EmailField()
    role_id = serializers.IntegerField()
