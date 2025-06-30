from rest_framework import serializers
from core.models import Projects

class ProjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id', 'name', 'description', 'created_by', 'created_at', 'updated_at']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id', 'name', 'description', 'created_by', 'created_at', 'updated_at']