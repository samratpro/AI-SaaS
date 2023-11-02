from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AppUser  # Replace with your custom user model

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'first_name', 'last_name', 'profile_image', 'activation_code')}),
        ('Permissions', {'fields': ('is_active', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(AppUser, CustomUserAdmin)
