from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
   
    is_renter = models.BooleanField('Is renter', default=False)
    is_landlord = models.BooleanField('Is landlord', default=False)
   
 




