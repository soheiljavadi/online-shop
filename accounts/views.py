from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from .models import user
from .serializer import *

# Create your views here.


class RegisterUserView(APIView):
    parser_classes = [JSONParser, MultiPartParser, FormParser]
    def post(self, request):

        # if email is already in use
        # if user.objects.filter(first_name=request.data['first_name']).exists():
        #     return Response({'error': 'Email already registered'}, status=status.HTTP_400_BAD_REQUEST)
      
        serializer = UserregisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserView(APIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get(self, request):
        serializer = UserregisterSerializer(request.user, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # update user profile image
class AllUsersView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        users = user.objects.all()
        serializer = UserregisterSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)