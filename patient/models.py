from django.db import models
from user.models import User

# Create your models here.
class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    sickness = models.CharField(max_length = 100)