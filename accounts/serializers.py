from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate
from rest_framework import status
import random
import uuid

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'phone', 'address', 'city', 'country', 'zip_code']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'address', 'city', 'country', 'zip_code']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        verification_code = str(random.randint(100000, 999999))  # Generate a 6-digit code
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            address=validated_data.get('address', ''),
            city=validated_data.get('city', ''),
            country=validated_data.get('country', ''),
            zip_code=validated_data.get('zip_code', ''),
            verification_code=verification_code,
            email_verified=False
        )
        return user
    
        

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid credentials")