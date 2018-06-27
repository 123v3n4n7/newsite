from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(max_length=32, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']


class UserAuthenticate(serializers.ModelSerializer):
    username = serializers.CharField(max_length=32)
    password = serializers.CharField(max_length=8, write_only=True)

    def create(self, data):
        user = authenticate(usernmae=data['username'], username=data['password'])

    class Meta:
        model = User
        fields = ['username', 'password']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']


class AuthCustomTokenSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=32)
    password = serializers.CharField(max_length=8, write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:

            user = authenticate(username=username, password=password)

            if user:
                if not user.is_active:
                    msg = ('User account is disabled.')
                    raise ValidationError(msg)
            else:
                msg = ('Unable to log in with provided credentials.')
                raise ValidationError(msg)
        else:
            msg = ('Must include "email or username" and "password"')
            raise ValidationError(msg)

        attrs['user'] = user
        return attrs
