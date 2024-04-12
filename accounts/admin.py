from django.contrib import admin
from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import user,usermanager

# Register your models here.
from django.contrib import admin
from django.contrib.auth import get_user_model

user=get_user_model()

admin.site.register(user)