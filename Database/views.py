from django.shortcuts import render
from .models import Property
 
def showproperty(request):
    properties = Property.objects
    return render(request, 'property.html', { 'propertys': properties } )