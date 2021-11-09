from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class TokenObtainPairWithoutPasswordSerializer(TokenObtainPairSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].required = False

    def validate(self, attrs):
        username = attrs.get('username')
        user, _ = User.objects.get_or_create(
            username=username,
            defaults={
                "password": ''
            }
        )
        authenticate(user)
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }


class GetCodeSerializer(serializers.Serializer):
    username = serializers.RegexField(regex=r"^[0][9][0-9]{9}$")
