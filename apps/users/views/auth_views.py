from rest_framework import generics, permissions
from apps.users.serializers.user_serializers import UserRegistrationSerializer, UserSerializer
from apps.users.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from apps.users.serializers.auth_serializers import LoginSerializer

class RegisterUserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]


class LoginAPIView(TokenObtainPairView):
    serializer_class = LoginSerializer


class UserProfileAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user