from django.urls import path
from .views import RegisterUserView, UserView, AllUsersView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,)
# from .views import home

app_name='accounts'
urlpatterns = [  path('', AllUsersView.as_view()),
    path('user/', UserView.as_view()),
    path('register/', RegisterUserView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    
]
