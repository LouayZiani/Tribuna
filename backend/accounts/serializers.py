from rest_framework import serializers
from django.contrib.auth.models import User

# serializers.Serializer — requirement #4a
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

# serializers.Serializer — requirement #4a
class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email    = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=6)

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('Username already taken.')
        return value

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )