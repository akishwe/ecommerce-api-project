from rest_framework import generics
from apps.users.models import User
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from apps.users.serializers.user_serializers import  UserRegistrationSerializer
from apps.users.serializers.auth_serializers import LoginSerializer
from apps.users.serializers.user_serializers import UserSerializer
from rest_framework.response import Response


class RegisterUserAPIView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]


class LoginAPIView(TokenObtainPairView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]


class UserProfileAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)