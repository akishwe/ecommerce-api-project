from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework import serializers
from apps.users.serializers.user_serializers import UserSerializer


class LoginSerializer(TokenObtainPairSerializer):

    username_field = "email"

    def validate(self, attrs):

        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(email=email, password=password)

        if not user:
            raise serializers.ValidationError("Invalid email or password")

        data = super().validate(attrs)

        user_data = UserSerializer(self.user).data

        return {
            "user": user_data,
            "tokens": {
                "access": data["access"],
                "refresh": data["refresh"],
            }
        }