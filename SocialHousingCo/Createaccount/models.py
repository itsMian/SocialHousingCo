from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
# Create your models here.

class Accounts(models.Model):
    Email = models.CharField (primary_key=True, max_length=50, default ='')
    password = models.CharField (max_length=20, default ='')
    confirmpassword = models.CharField (max_length=20, default ='')
    role = models.CharField (max_length=10, default='')

class setupprofilerenter(models.Model):
    Email = models.ForeignKey ("Accounts", on_delete=models.CASCADE)
    fname = models.CharField ( max_length=20, default ='')
    lname = models.CharField (max_length=20, default ='')
    dob = models.DateField (max_length=20, default ='')
    income = models.IntegerField(default='0')
    reason = models.CharField ( max_length=250, default ='')


