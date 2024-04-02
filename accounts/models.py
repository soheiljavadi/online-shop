from typing import Any
from django.db import models
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password

# Create your models here.get("")

class usermanager(BaseUserManager):
    def _create_user(self,email,password,**extra_fields):

        if not email:
            raise ValueError("thw given email must be set")
        email=self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.password=make_password(password)
        user.save(using=self._db)
        return user
        
    
    def create_user(self,email,password=None,**extra_fields):
        extra_fields.setdefault("is_staff",False)
        extra_fields.setdefault("is_superuser",False)
        return self._create_user(email,password,**extra_fields)
    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError ("is_staff should true") 
        if extra_fields.get("is_superuser") is not True:
            raise ValueError ("is_superuser should true") 
        return self._create_user(email,password,**extra_fields)
        


class user(AbstractBaseUser,PermissionsMixin):
    first_name=models.CharField(('name'),max_length=100,blank=True)

    last_name=models.CharField(('last name'),max_length=100,blank=True)

    email=models.EmailField(("email addres"),unique=True)

    mobile=models.CharField(("mobile"),max_length=11,unique=True,blank=True,null=True)

    is_staff=models.BooleanField(_('staff status'),default=False)
    is_active=models.BooleanField(('active'),default=True)
    date_joined=models.DateTimeField(('date joined'),default=timezone.now)

    objects=usermanager()
    EMAIL_FIELD='email'
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    class meta:
        verbose_name=_('user')
        verbose_name_plural=_("users")
        

    def clean(self) -> None:
         super().clean()
         self.email=self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        full_name="%s%s"%(self.first_name,self.last_name)
        return full_name.strip()
    
    def get_short_name(self):
        return self.first_name
    
    def email_user(self,subject,message,from_email=None,**kwargs):
        send_mail(subject,message,from_email,[self.email],**kwargs)

