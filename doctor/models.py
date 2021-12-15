from django.db import models
from user.models import User

# Create your models here.

specilisation =(
    ('MBBS' , 'MBBS'),
    ('MS' , 'MS'),
    ('MD' , 'MD'),
    ('BAMS' , 'BAMS'),
    ('BPT' , 'BPT'),
    ('BUMS' , 'BUMS'),
)


class Doctor(User):
    specialisation = models.CharField(max_length =100,choices=specilisation,null=True)
    experience = models.PositiveIntegerField()