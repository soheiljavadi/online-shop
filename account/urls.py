from django.urls import path, include
from .views import register_user,profile,updateProfile,register_seller,MyTokenObtainPairView,TokenRefreshView





app_name='account'
urlpatterns = [
path('register',register_user.as_view(),name='register'),
path('profile',profile,name='profile'),
path('updateprofile',updateProfile,name='updateprofile'),
path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),]