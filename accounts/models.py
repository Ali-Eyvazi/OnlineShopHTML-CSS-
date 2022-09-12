from django.db import models
from django.contrib.auth.models import AbstractBaseUser ,PermissionsMixin
from .managers import UserManager


class User(AbstractBaseUser,PermissionsMixin): # creating user model 
    email=models.EmailField(max_length=100,unique=True)
    phone_number=models.CharField(max_length=11,unique=True)
    full_name=models.CharField(max_length=50)
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)



    objects=UserManager() #manager  is located in an other app in the same dir

    USERNAME_FIELD='phone_number'    # log in field
    REQUIRED_FIELDS= ['email','full_name']   

    def __str__(self) -> str:
        return self.email


   
    @property
    def is_staff(self):
        return self.is_admin




class OtpCode(models.Model):
    phone_number=models.CharField(max_length=11 ,unique=True)
    code=models.PositiveSmallIntegerField()
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.phone_number}-{self.code}-{self.created}'










    
