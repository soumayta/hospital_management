from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
import uuid

# Create your models here.

gender = (
    ('Male' , 'Male'),
    ('Female' , 'Female'),
)



class User(AbstractUser):
    id = models.UUIDField(primary_key = True, editable = False)
    age = models.IntegerField()
    gender = models.CharField(max_length=10,choices=gender,null=True)
    city = models.CharField(max_length=10)
    address = models.CharField(max_length=40)
    mobile = models.IntegerField()
    dob = models.DateField('date of birth')
    

    def __str__(self):
        return str(self.name)


    
    

    
    




