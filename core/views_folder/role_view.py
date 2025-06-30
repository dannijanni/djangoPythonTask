from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models import Roles
from core.serializers.role_Serilaizer import RoleSerializer
from django.shortcuts import get_object_or_404

class CreateRole(APIView):
    def post(self, request):
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            if Roles.objects.filter(name=serializer.validated_data['name']).exists():
                return Response({"detail": "Role with this name already exists"}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListRoles(APIView):
    def get(self, request):
        roles = Roles.objects.all()
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GetRoleById(APIView):
    def get(self, request, role_id):
        role = get_object_or_404(Roles, id=role_id)
        serializer = RoleSerializer(role)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UpdateRoleById(APIView):
    def put(self, request, role_id):
        role = get_object_or_404(Roles, id=role_id)
        serializer = RoleSerializer(role, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteRoleById(APIView):
    def delete(self, request, role_id):
        role = get_object_or_404(Roles, id=role_id)
        role.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

