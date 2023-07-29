from rest_framework import serializers
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "name", "phone", 'verification_code')


class VerificationSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=4)


class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField()


class UsersListSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    phone = serializers.CharField()

    class Meta:
        model = User
        fields = ['id', 'name', 'phone', 'role']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'phone',
        ]
