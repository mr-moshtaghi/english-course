from django.contrib import admin

from account.models import CustomUser, VerificationCode


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['cellphone', 'first_name', 'last_name']
    search_fields = ['first_name', 'last_name']


class VerificationCodeAdmin(admin.ModelAdmin):
    list_display = ['code', 'cellphone', 'expire_time', 'last_send']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(VerificationCode, VerificationCodeAdmin)
