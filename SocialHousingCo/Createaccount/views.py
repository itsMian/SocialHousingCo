from collections import UserDict
from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


from django.http import HttpResponse


def index(request):  
    return render(request, 'createaccount.html')

def Accounts(request):
    Accounts = Accounts.objects
    return render (request,'createaccount.html', {'Accounts': Accounts})




