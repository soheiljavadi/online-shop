from django.contrib import admin
from .models import *
@admin.register(Costomuser)
class adminuser(admin.ModelAdmin):
    pass