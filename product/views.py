from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializer import *
import stripe
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .permission import IsAdminOrSeller
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from .serializer import  CommentModelSerializer, LikeSerializer
from rest_framework import generics


class ProductViewSet (viewsets.ModelViewSet):
      queryset = product.objects.all()
      serializer_class = ProductSerializer
      permission_classes = [IsAdminOrSeller]


class ProductapiViewSet (viewsets.ModelViewSet):
      queryset = product.objects.all()
      serializer_class = ProductSerializer

class CommentListCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class =  CommentModelSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LikeCreateDelete(generics.CreateAPIView, generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        like = Like.objects.filter(product_id=kwargs['product_id'], user=self.request.user).first()
        if like:
            like.delete()
            return Response({'message': 'Unlike successful'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error': 'Like not found'}, status=status.HTTP_404_NOT_FOUND)
        



class cartviewset(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    def list(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        serializer = cartserializer(cart)
        return Response(serializer.data)

    def add_item(self, request):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)
        
        try:
            product = product.objects.get(id=product_id)
        except product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        return Response({'status': 'item added to cart'})

    def remove_item(self, request, pk=None):
        try:
            cart_item = CartItem.objects.get(id=pk, cart__user=request.user)
        except CartItem.DoesNotExist:
            return Response({'error': 'Item not found in your cart'}, status=status.HTTP_404_NOT_FOUND)

        cart_item.delete()
        return Response({'status': 'item removed from cart'})

    def clear_cart(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart.items.all().delete()
        return Response({'status': 'cart cleared'})

   
    