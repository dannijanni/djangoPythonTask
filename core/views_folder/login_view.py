# core/views/auth.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.models import Users
from core.security import verify_password
from core.schemas.auth import LoginRequestSerializer, LoginResponseSerializer

class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginRequestSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            try:
                user = Users.objects.get(email=email)
            except Users.DoesNotExist:
                return Response({"detail": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)

            if not verify_password(password, user.password_hash):
                return Response({"detail": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)

            response_data = {
                "id": user.id,
                "full_name": user.full_name,
                "email": user.email,
                "role_id": user.role_id,  # Use role_id_id since it's a ForeignKey
            }

            return Response(response_data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
