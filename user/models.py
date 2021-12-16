from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.

gender = (
    ('Male' , 'Male'),
    ('Female' , 'Female'),
)



class User(AbstractUser):
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=10,choices=gender)
    city = models.CharField(max_length=10)
    address = models.CharField(max_length=40)
    mobile = models.IntegerField()
    dob = models.DateField(max_length=10)
    

    def __str__(self):
        return str(self.name)


    
    

    
    




