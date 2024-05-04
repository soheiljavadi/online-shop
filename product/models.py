from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
from django.urls import reverse
from django.conf import settings

from django.contrib.auth.models import User

from account.models import Costomuser

class Brand(models.Model):
    name = models.CharField(_("Name"), max_length=150)
    en_name = models.CharField(_("English Name"), max_length=150)
    slug = models.SlugField(_("Slug"))

    def __str__(self) -> str:
        return self.slug


class MyQuerySet(models.QuerySet):
    def delete(self):
        return self.update(is_active=False)


class NoDeleteManager(models.Manager):
    def get_queryset(self):
        return MyQuerySet(self.model, using=self._db)
    
    



class product(models.Model):

    name=models.CharField(_('Name'),max_length=100)
   

    slug=models.SlugField(_('Slug'),default='slug')
    
    Category = models.ForeignKey("Category",
                                 verbose_name=_("Category"),on_delete=models.RESTRICT,null=True)
    
    price = models.DecimalField(max_digits=10, decimal_places=2)
    

    brand = models.ForeignKey("Brand", verbose_name=_("Brand"),on_delete=models.SET_NULL,null=True,blank=True)
  
    is_active = models.BooleanField(_("is active"), default=True)

    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    
    objects = NoDeleteManager()
   


class Like(models.Model):
      product = models.ForeignKey('Product', related_name='likes', on_delete=models.CASCADE)
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #   created_at = models.DateTimeField(auto_now_add=True)


      class Meta:
        unique_together = ('product', 'user')  
      def __str__(self):
        return f'{self.user.first_name} likes {self.product.name}'
      
      def number_of_likes(self):
        return self.like.count()



class Category(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    slug = models.SlugField(_("Slug"), unique=True, db_index=True)
    description = models.TextField(_("Description"))
    icon = models.ImageField(
        _("Icon"), upload_to='category_images', null=True, blank=True)
    image = models.ImageField(
        _("Image"), upload_to='category_images', null=True, blank=True)
    parent = models.ForeignKey("self",
                               verbose_name=_("Parent Category"),
                               on_delete=models.SET_NULL,
                               null=True,
                               blank=True
                               )

  
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


    def __str__(self) -> str:
        return self.slug
class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)



    def __str__(self):
        return f"{self.user}'s Shopping Cart"
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    paid = models.BooleanField(default=False)
    total_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def total_price(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
    
class Payment(models.Model):
    order = models.OneToOneField('cart', related_name='payment', on_delete=models.CASCADE)
    stripe_charge_id = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment of ${self.amount} for Order {self.order.id}"

class Comment(models.Model):
    product = models.ForeignKey('Product', related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    content = models.TextField(default='hello')
   
    def __str__(self):
        return f'Comment by {self.user.first_name} on {self.product.name}'


