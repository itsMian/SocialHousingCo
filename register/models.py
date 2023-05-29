from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
   
    is_renter = models.BooleanField('Is renter', default=False)
    is_landlord = models.BooleanField('Is landlord', default=False)

    dob = models.CharField(max_length=10, default='')
    phone = models.CharField(max_length=10, default='')
    aboutme = models.CharField(max_length=2000, default='')

    income_type = models.CharField(max_length=20, default='')
    pay_frequency = models.CharField(max_length=20, default='')
    amount_after_tax = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    
    




