from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models import Projects, Users
from core.serializers.project_serializer import ProjectCreateSerializer, ProjectSerializer
from django.shortcuts import get_object_or_404

class CreateProject(APIView):
    def post(self, request):
        print("🔥 Remapped user data:", request.data)
        serializer = ProjectCreateSerializer(data=request.data)
        if serializer.is_valid():
            created_by = serializer.validated_data.get("created_by")
            if not Users.objects.filter(id=created_by.id).exists():
                return Response({"detail": "Creator user not found"}, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetAllProjects(APIView):
    def get(self, request):
        projects = Projects.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GetProjectById(APIView):
    def get(self, request, project_id):
        project = get_object_or_404(Projects, id=project_id)
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UpdateProjectById(APIView):
    def put(self, request, project_id):
        project = get_object_or_404(Projects, id=project_id)
        serializer = ProjectCreateSerializer(project, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteProjectById(APIView):
    def delete(self, request, project_id):
        project = get_object_or_404(Projects, id=project_id)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

