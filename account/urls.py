from django.urls import path, include
from .views import MyTokenObtainPairView,TokenRefreshView,register_user,profile,updateProfile,register_seller





app_name='account'
urlpatterns = [path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
path('register',register_user.as_view(),name='register'),
path('profile',profile,name='profile'),
path('updateprofile',updateProfile,name='updateprofile')]