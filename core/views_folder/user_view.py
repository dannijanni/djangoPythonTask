# # core/views/users.py

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from core.models import Users
# from core.serializers.user_serializer import UserCreateSerializer, UserSerializer
# from core.security import verify_password
# from django.shortcuts import get_object_or_404

# class CreateUser(APIView):
#     def post(self, request):
#         serializer = UserCreateSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class LoginUser(APIView):
#     def post(self, request):
#         email = request.data.get("email")
#         password = request.data.get("password")
#         user = get_object_or_404(Users, email=email)

#         if not verify_password(password, user.password_hash):
#             return Response({"detail": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)

#         return Response({
#             "id": user.id,
#             "full_name": user.full_name,
#             "email": user.email,
#             "role_id": user.role.id
#         }, status=status.HTTP_200_OK)




from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models import Roles, Users
from core.serializers.user_serializer import UserCreateSerializer, UserSerializer
from core.security import hash_password, verify_password
from django.shortcuts import get_object_or_404

class CreateUser(APIView):
    def post(self, request):
        data = request.data.copy()

        # Remap fields if necessary
        if 'name' in data:
            data['full_name'] = data.pop('name')
        if 'email' in data:
            data['email'] = data.pop('email')
        if 'password' in data:
            data['password_hash'] = data.pop('password')
        if 'role_id' in data:
            data['role'] = data.pop('role_id')  # Keep as role_id

        # Debug: Print before serialization
        print("🔥 Remapped user data:", data)


        serializer = UserCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        print("❌ User serializer errors:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginUser(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = get_object_or_404(Users, email=email)

        if not verify_password(password, user.password_hash):
            return Response({"detail": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)

        return Response({
            "id": user.id,
            "full_name": user.full_name,
            "email": user.email,
            "role_id": user.role.id
        }, status=status.HTTP_200_OK)


class GetAllUsers(APIView):
    def get(self, request):
        users = Users.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserDetailUpdateDelete(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(Users, id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, user_id):
        user = get_object_or_404(Users, id=user_id)
        data = request.data.copy()

        # If password is being updated, hash it
        if "password_hash" in data:
            data["password_hash"] = hash_password(data["password_hash"])

        serializer = UserCreateSerializer(user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id):
        user = get_object_or_404(Users, id=user_id)
        user.delete()
        return Response({"detail": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
