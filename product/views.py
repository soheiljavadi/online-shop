
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

stripe.api_key = settings.STRIPE_SECRET_KEY
class PaymentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, cart_id):
        order = Cart.objects.get(id=cart_id, user=request.user)  # Make sure to check ownership and order status
        serializer = PaymentSerializer(data=request.data)
        
        if serializer.is_valid():
            token = serializer.validated_data['token']
            try:
                charge = stripe.Charge.create(
                    amount=int(order.total /10),  # Amount in cents
                    currency='usd',
                    description=f'Charge for Order {order.id}',
                    source=token
                )

                Payment.objects.create(
                    order=order,
                    stripe_charge_id=charge.id,
                    amount=order.total
                )

                order.status = 'paid'
                order.save()

                return Response({'message': 'Payment successful'}, status=status.HTTP_201_CREATED)
            except stripe.error.StripeError as e:
                return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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