from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', required=True)
    password = serializers.CharField(write_only=True, required=True)
    department = serializers.ChoiceField(choices=[('dev', 'Developer'), ('tester', 'Tester'), ('designer', 'Designer'), ('devops', 'DevOps'), ('business analysis', 'Business Analysis')])

    class Meta:
        model = Employee
        fields = ['username', 'password', 'department']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user_data = validated_data.pop('user')

        username = user_data.get('username')
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({"username": "User already exists"})

        user = User(**user_data)
        user.set_password(password)
        user.save()

        employee = Employee.objects.create(user=user, **validated_data)
        return employee

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                attrs['user'] = user
                return attrs
            else:
                raise serializers.ValidationError("Wrong username or password")
        else:
            raise serializers.ValidationError("Username and password required")

    def create(self, validated_data):
        user = validated_data['user']
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }