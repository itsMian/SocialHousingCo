from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import logout



def index(request):
    return render(request, 'profile.html')


def land(request):
    return render(request, 'landlord.html')

def personal(request):
    return render(request, 'personal-details.html')

def aboutme(request):
    return render(request, 'aboutme.html')

def identity(request):
    return render(request, 'identity-documents.html')




def logout_view(request):
    logout(request)
    return redirect('/')  