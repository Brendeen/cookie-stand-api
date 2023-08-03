from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)  # adds in password encryption
        user.save()
        return user

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password', 'email')  # can also use __all__
