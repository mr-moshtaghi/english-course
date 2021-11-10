import datetime

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import VerificationCode
from english_course import settings
from account.serializers import GetCodeSerializer


class GetCodeView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = GetCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cellphone = serializer.validated_data['cellphone']
        login_code = VerificationCode.objects.filter(
            last_send__gte=(datetime.datetime.now() - datetime.timedelta(
                seconds=settings.RESEND_WAITE_TIME)),
            cellphone=cellphone).first()

        if login_code:
            return Response(
                {'Bad Request': "Your request is detected as duplicate request please wait or try again later"},
                status=status.HTTP_400_BAD_REQUEST
            )

        VerificationCode.create_code(cellphone=cellphone)
        return Response(
            data=serializer.data, status=status.HTTP_201_CREATED
        )
