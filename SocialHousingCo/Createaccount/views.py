from collections import UserDict
from urllib import request

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from Createaccount.models import Accounts, setupprofilerenter
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View


from django.http import HttpResponse


def index(request):  
    return render(request, 'createaccount.html')

def registry(request):
    Accounts = Accounts.objects
    return render (request,'createaccount.html', {'Accounts': Accounts})


@csrf_protect
def register(request):
    acc = Accounts()
    acc.Email = request.POST.get('Email')
    acc.password = request.POST.get('password')
    acc.confirmpassword = request.POST.get('confirmpassword')
    acc.role = request.POST.get('role')
    acc.save()
    messages.success(request, "Account successfully created")
    return redirect('/login')

class setupprofile(View):
    def get(self, request, *args, **kwargs):
        Accounts = get_object_or_404(Accounts, id=kwargs['Email'])
        context = {'Accounts': Accounts}
        return render(request, 'setupaccount.html', context)
    

@csrf_protect
def createprofile(request):
     cp = setupprofilerenter()
     cp.Email = request.POST.get('Email')
     cp.fname = request.POST.get('fname')
     cp.lname = request.POST.get('lname')
     cp.dob = request.POST.get('dob')
     cp.income = request.POST.get('income')
     cp.reason = request.POST.get('reason')
     cp.save()
     messages.success(request, "Profile successfully updated")
     return redirect('/profiles')


