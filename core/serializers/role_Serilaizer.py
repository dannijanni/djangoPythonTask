from rest_framework import serializers
from core.models import Roles

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = ['id', 'name']