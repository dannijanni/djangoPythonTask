from rest_framework import serializers
from core.models import Tasks
from core.models import Tasks, Projects, Users

# class TaskCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tasks
#         fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id', 'name']  # Include whatever fields you need

class TaskSerializer(serializers.ModelSerializer):
    project = ProjectSerializer()  # Nested serializer for project
    
    class Meta:
        model = Tasks
        fields = '__all__'

class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = [
            'title',
            'description',
            'project',      # FK project id
            'created_by',   # FK user id
            'closed_by',    # FK user id (mapped from assignedTo)
            'due_date',
            'priority',
            'status',
        ]

