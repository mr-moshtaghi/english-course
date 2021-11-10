import datetime
import random

from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _
from django.db import models
from kavenegar import *

from account.usermanager import UserManager
from core.models import BaseModel
from english_course import settings


@deconstructible
class NumericUsernameValidator(validators.RegexValidator):
    regex = r"^[0][9][0-9]{9}$"
    message = _(
        'Enter a valid username. This value must be 11 numbers'
    )
    flags = 0


class CustomUser(AbstractUser):
    username = None
    objects = UserManager()
    cellphone_validator = NumericUsernameValidator()
    cellphone = models.CharField(
        _('username'),
        max_length=11,
        unique=True,
        help_text=_('Required. 11 digits for cellphone.'),
        validators=[cellphone_validator],
        error_messages={
            'unique': _("A user with that cellphone already exists."),
        },
    )
    USERNAME_FIELD = 'cellphone'
    REQUIRED_FIELDS = []


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

