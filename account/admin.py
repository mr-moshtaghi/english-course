from django.contrib import admin

from account.models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name']
    search_fields = ['username', 'first_name', 'last_name']


admin.site.register(CustomUser, CustomUserAdmin)
