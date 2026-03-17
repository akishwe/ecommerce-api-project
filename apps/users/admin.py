from django.contrib import admin
from .models import User, UserAddress

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "username", "role", "is_active")

@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "street", "city", "is_default")