from django.db import models

from core.models import BaseModel


class VerificationCode(BaseModel):
    code = models.CharField(max_length=20)
    cellphone = models.CharField(max_length=20, null=True, blank=True)
    expire_time = models.DateTimeField(null=True, blank=True)
    last_send = models.DateTimeField(null=True, blank=True)