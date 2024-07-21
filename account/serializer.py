from .models import *
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
import django.contrib.auth.password_validation as validators
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,)

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer 
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

      
        token['first_name'] = user.first_name
        token['email'] = user.email

#         return token
class SellerRegistrationSerializer(serializers.ModelSerializer):
     password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
     password2 = serializers.CharField(write_only=True, required=True)

     class Meta:
        model = Costomuser
        fields = ('first_name', 'username','last_name','email','password','password2','company_name')
       


     def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        

        def create(self, validated_data):
         validated_data['is_seller'] = True  # Automatically set users as sellers
         return super().create(validated_data)
       
        
     
    

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    # password2 = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = Costomuser
        fields = ('first_name','username','last_name','email','password')
     

       
    # def validate(self, attrs):
    #     if attrs['password'] != attrs['password2']:
    #         raise serializers.ValidationError(
    #             {"password": "Password fields didn't match."})

    #     return attrs
    

    def create(self, validated_data):

        user=Costomuser(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class profile(serializers.ModelSerializer):
    class Meta:
        model=Costomuser
        fields=('first_name','last_name')

