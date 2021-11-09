import datetime
import random

from django.db import models
from kavenegar import *

from core.models import BaseModel
from english_course import settings


class VerificationCode(BaseModel):
    code = models.CharField(max_length=20)
    cellphone = models.CharField(max_length=20, null=True, blank=True)
    expire_time = models.DateTimeField(null=True, blank=True)
    last_send = models.DateTimeField(null=True, blank=True)

    @classmethod
    def create_code(cls, cellphone=None):
        code = random.randint(10 ** (settings.CODE_LENGTH - 1),
                              10 ** settings.CODE_LENGTH)
        verification_code = cls(
            cellphone=cellphone,
            code=code,
            expire_time=datetime.datetime.now() + datetime.timedelta(
                        minutes=settings.CODE_EXPIRE_TIME),
            last_send=datetime.datetime.now()
        )
        verification_code.save()
        verification_code.send_sms()
        return verification_code

    def send_sms(self):
        try:
            api_kavenegar = KavenegarAPI(settings.KAVENEGAR_API_KEY)
            params = {
                'receptor': self.cellphone,
                'token': self.code,
                'template': "khanebazia"
            }
            response = api_kavenegar.verify_lookup(params)
            print(response)
        except APIException as e:
            print(e)
        except HTTPException as e:
            print(e)
