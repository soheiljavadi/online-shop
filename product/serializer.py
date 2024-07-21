from .models import *
from rest_framework import serializers

class CommentModelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('content'
                  'product',
                  'user')
        read_only_fields = ('user', 'product')
        model = Comment

    def create(self, validated_data):
        return super().create(validated_data)


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Brand


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Category

class cartserializer(serializers.ModelSerializer):

    class Meta:
        model=Cart
        fields=['user']



class ProductSerializer(serializers.ModelSerializer):
     brand_details = BrandSerializer(source='brand', read_only=True)
     category_details = CategorySerializer(source='category', read_only=True)
     

     class Meta:
        model = product
        fields = ['id', 'name', 'price','category_details','brand_details']

class cartitemserializer(serializers.ModelSerializer):
    order=cartserializer(source='cart',read_only=True)
    product=ProductSerializer(source='product',read_only=True)
    class Meta:
        model=CartItem
        fields=['cart','product','total_paid','quantity']



class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'product', 'user']
    
