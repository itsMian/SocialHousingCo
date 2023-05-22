from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings

# Create your models here.

class Property(models.Model):
    image = models.FileField(upload_to='image/', blank=True, default='settings.MEDIA_ROOT/image/unknown_prop.png')
    title = models.CharField(max_length=400, default='Title')
    address = models.CharField(max_length=200, default='')
    suburb = models.CharField(max_length=200, default='')
    state = models.CharField(max_length=200, default='')
    postcode = models.IntegerField(default='0')
    price = models.IntegerField(default='0')
    description = models.TextField(default='Description')
    bedroom = models.IntegerField(default='0')
    bathroom = models.IntegerField(default='0')
    parking_space = models.IntegerField(default='0')

    class Meta:
       verbose_name_plural = 'Properties'