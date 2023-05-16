from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
# Create your models here.

class Accounts(models.Model):
    Email = models.CharField (max_length=50, default ='')
    password = models.CharField (max_length=20, default ='')
    confirmpassword = models.CharField (max_length=20, default ='')
