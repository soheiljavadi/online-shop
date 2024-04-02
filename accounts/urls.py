
from django.urls import path, include
# from .views import home

app_name='accounts'
urlpatterns = [
    path('api-auth/',include(('rest_framework.urls','accounts'))),
    
]
