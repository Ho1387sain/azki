from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth import authenticate









class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'number']  


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    def validate(self, value):
        username = value.get('username')
        password = value.get('password')

        user = authenticate(username=username, password=password)
      

        value['user'] = user
        return value
    