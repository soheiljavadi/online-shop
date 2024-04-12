from rest_framework import serializers
from .models import user

class UserregisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('username','password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        users = user.objects.create_user(**validated_data)
        
        return users

class Userinfoserilizer(serializers.ModelSerializer):
    pass
    
   



