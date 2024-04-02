from django.contrib import admin
from .views import product_detail
from django.urls import path
app_name='product'
urlpatterns = [
    path('admin/',admin.site.urls),
    path('<int:pk>/',product_detail)
]
