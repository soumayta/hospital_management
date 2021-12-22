from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.

GENDER = (
    ('Male' , 'Male'),
    ('Female' , 'Female'),
)
PROFILE=(
    ('Doctor' , 'Doctor'),
    ('Patient' , 'Patient'),
)

class User(AbstractUser):
    age = models.IntegerField(blank=True, default=None, null=True)
    gender = models.CharField(max_length=10,choices=GENDER,default='Male')
    city = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=40, null=True)
    mobile = models.IntegerField(null=True)
    dob = models.DateField(max_length=10, null=True)
    profile = models.CharField(max_length=10,choices=PROFILE,default='Doctor')
    

    
    


    
    

    
    




