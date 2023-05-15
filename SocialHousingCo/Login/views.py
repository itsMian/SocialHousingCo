from django.shortcuts import render


from django.http import HttpResponse


def index(request):
    return render(request, 'login.html')

def landlordlogin(request):
    return render(request, 'landlordlogin.html')


