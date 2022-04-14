from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.exceptions import APIException
from rest_framework_simplejwt.tokens import RefreshToken

from apps.user.models import User


class MyAuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField(
        write_only=True
    )
    password = serializers.CharField(
        write_only=True
    )

    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = User.objects.filter(email=email).first()
        if not user:
            custom_data = {
                "status": False,
                "message": 'User not registered.',
            }
            raise APIException(custom_data)
        else:
            if user.check_password(password):
                refresh = self.get_token(user)
                access = str(refresh.access_token)
                refresh = str(refresh)
                custom_data = {
                    "status": True,
                    "message": 'Token Generated.',
                    "data": {
                        "access": access,
                        "refresh": refresh
                    }
                }
                return custom_data


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'password']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)
