from rest_framework import serializers
from mainApp import models
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_active']


class AccountSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = models.Account
        fields = ['id', 'user']


class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']


class CreateAccountSerializer(serializers.ModelSerializer):
    user = CreateUserSerializer()

    class Meta:
        model = models.Account
        fields = ['user']

    def create(self, validated_data):
        user = validated_data.get('user')
        user = User.objects.create_user(username=user.get('username'), email=user.get('email'),
                                        password=user.get('password'))
        return models.Account.objects.create(user=user)

class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Password
        fields = ['site', 'password']