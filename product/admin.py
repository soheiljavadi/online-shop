from django.contrib import admin
from django.contrib import admin
from .models import product, Category, Comment,\
Cart,CartItem

admin.site.register(product)
admin.site.register(Cart)
admin.site.register(CartItem)