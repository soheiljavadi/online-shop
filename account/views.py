from django.shortcuts import render
from rest_framework.generics import  CreateAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,)
from .serializer import *
from .models import *
# Create your views here.

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class register_user(CreateAPIView):
    serializer_class=RegisterSerializer
    queryset=Costomuser.objects.all()

class register_seller(CreateAPIView):
    serializer_class=SellerRegistrationSerializer
    queryset=Costomuser.objects.filter(is_seller=True)   

@api_view([ "GET"])
@permission_classes([IsAuthenticated])
def profile(request):
    user=request.user
    serializer = profile(instance=user, )
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateProfile(request):
    user = request.user
    serializer = profile(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
