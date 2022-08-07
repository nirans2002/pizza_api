from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
# from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

class CustomUserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError('email cannot be empty')
        
        email = self.normalize_email(email)
        # create new_user
        new_user = self.model(email=email,*extra_fields)
        # set default password for new user 
        new_user.set_password(password)
        new_user.save()

        return new_user


    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser must have is_active=True')

        return self.create_user(email,password,**extra_fields)


class CustomUser(AbstractUser):
    username = models.CharField(max_length=50 , unique=True)
    email = models.EmailField(max_length=255 , unique=True)
    phone_no = PhoneNumberField(null=False,unique=True)

    USERNAME_FIELD = 'email'   # username field is email

    REQUIRED_FIELDS = ['username','phone_no']

    objects = CustomUserManager()

    def __str__(self) -> str:
        return f"<user  {self.email}>"