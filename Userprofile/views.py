from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Profiles
from .forms import IncomeForm


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

def income_create(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            # Assuming the user is logged in and the Profiles instance is linked to User
            profile = Profiles.objects.get(user=request.user)
            income = form.save(commit=False)
            income.profile = profile
            income.save()
            return redirect('profiles')
    else:
        form = IncomeForm()
    return render(request, 'income.html', {'form': form})


def referal_letter(request):
    return render(request, 'referal-letter.html')