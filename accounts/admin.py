from django.contrib import admin
from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import user,usermanager

# Register your models here.
class UserAdmin(BaseUserAdmin):
    list_display = []
    ordering = ['email']
    search_fields = ['full_name', 'email']
    readonly_fields = ['last_login', 'date_joined']

admin.site.register(user, UserAdmin)