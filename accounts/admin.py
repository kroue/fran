from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('address', 'city', 'country', 'zip_code')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('address', 'city', 'country', 'zip_code')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)