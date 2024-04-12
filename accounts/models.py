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
     def _create_user(self, username, password, **extra_fields):
        """
        Create and save a user with the given email, and password.
        """
        if not username:
            raise ValueError("The given email must be set")
        
        user = self.model(username, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user
     
     def create_user(self, username, password=None):
        

        user = self.model(username=username)

        user.set_password(password)
        user.save(using=self._db)

        return user
     
     def create_superuser(self, username,password=None, **extra_fields):
        user_admin=self.create_user(
            username,
            password=password
        )
        is_staff=True
        user_admin.is_admin = True
        user_admin.save(using=self._db)
        return user_admin
class user(AbstractBaseUser,PermissionsMixin):
    id = models.AutoField(primary_key=True)

    username = models.CharField(max_length=255, unique=True)
    password=models.CharField(('password'),max_length=6)

    
    

    mobile=models.CharField(("mobile"),max_length=11,unique=True,blank=True,null=True)

    is_staff=models.BooleanField(_('staff status'),default=False)
    is_active=models.BooleanField(('active'),default=True)
    date_joined=models.DateTimeField(('date joined'),default=timezone.now)

    objects=usermanager()
    USERNAME_FIELD='username'
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

