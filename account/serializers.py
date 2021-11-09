from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from account.models import CustomUser


class TokenObtainPairWithoutPasswordSerializer(TokenObtainPairSerializer):
    cellphone = serializers.CharField()
    code = serializers.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].required = False
        self.fields['username'].required = False

    def validate(self, attrs):
        cellphone = attrs.get('cellphone')
        user, _ = CustomUser.objects.get_or_create(
            cellphone=cellphone,
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
