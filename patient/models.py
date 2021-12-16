from django.db import models
from user.models import User

# Create your models here.
class Patient(User):
    sickness = models.CharField(max_length = 100)