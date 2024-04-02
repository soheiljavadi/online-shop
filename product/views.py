from django.shortcuts import render,get_object_or_404, redirect
from .models import product,Category

# Create your views here.
def product_detail(request,pk):
    p=get_object_or_404(product,id=pk)
    c=product.objects.select_related('Category')
    context={'product':p,
             'Category':c}

    return render(template_name= 'product/product_detail.html',context=context,request=request)
