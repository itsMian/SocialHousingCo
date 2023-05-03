from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'listpage.html')

def detailspage(request):
    return render(request, 'detailspage.html')