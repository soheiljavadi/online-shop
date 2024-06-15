from django.contrib import admin
from .views import *


from django.urls import path
app_name='product'
urlpatterns = [
    path('admin/',admin.site.urls),
        path('products/', ProductViewSet.as_view({
        'get': 'list',   # For getting a list of products
        'post': 'create', # For creating a new product
         'delete': 'destroy'
    })),
    # Handling retrieve, update and delete actions
    path('products/<int:pk>/', ProductapiViewSet.as_view({
        'get': 'retrieve',    # For getting a single product
      
    })),
     
     path('comments/', CommentListCreate.as_view(), name='comment_list_create'),
     path('likes/<int:product_id>/', LikeCreateDelete.as_view(), name='like_create_delete'),
    
]

