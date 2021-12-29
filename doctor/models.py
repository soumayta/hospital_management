from django.db import models
from user.models import User
from django.db import connections
# Create your models here.

SPECILISATION =(
    ('ANESTHESIOLOGIST' , 'ANESTHESIOLOGIST'),
    ('CARDIOLOGISTS' , 'CARDIOLOGISTS'),
    ('DERMATOTLOGIST' ,'DERMATOTLOGIST'),
    ('GASTROENTROLOGIST' , 'GASTROENTROLOGIST'),
    ('HEMATOLOGIST' , 'HEMATOLOGIST'),
    ('INTERNISTS' , 'INTERNISTS'),
)


class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    specialisation = models.CharField(max_length =100,choices=SPECILISATION,null=True)
    experience = models.PositiveIntegerField(null=True,blank=True)

    
    def __str__(self):
        return str(self.user.username)  
