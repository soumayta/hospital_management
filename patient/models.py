from django.db import models
from user.models import User
from doctor.models import Doctor                                        

# Create your models here.
class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    sickness = models.CharField(max_length = 100)
