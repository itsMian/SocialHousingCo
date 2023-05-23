from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from Database.models import Property
from django.http import Http404
from django.views import View
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect




def home(request):
    return render(request, 'homepage.html')