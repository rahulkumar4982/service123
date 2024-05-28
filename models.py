from django.db import models
from django.contrib.auth.models import User

class CustomUser(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(default='')
    phone_number = models.CharField(max_length=15)
    username = models.CharField(default='', max_length=50, unique=True)
    password = models.CharField(default='', max_length=128)
    #abstract = False

    def __str__(self):
       return f"{self.phone_number}{self.full_name}"
    
class User(models.Model):
    username = models.CharField(default='', max_length=255)
    password = models.CharField(default='', max_length=255)
    email = models.EmailField(default='')

    def __str__(self):
        return f"{self.username}{self.password}"