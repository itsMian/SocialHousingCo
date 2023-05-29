from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Profiles
from register.models import User
from .forms import IncomeForm
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect


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

@csrf_protect
def update_details(request):
    user = request.user
    user.first_name = request.POST.get('first-name')
    user.last_name = request.POST.get('last-name')
    user.dob = request.POST.get('date-of-birth')
    user.phone = request.POST.get('phone-number')
    user.save()
    if user.is_landlord:
        return redirect('/profiles/landlord/')
    else:
        return redirect('/profiles/')
    
@csrf_protect
def update_aboutme(request):
    user = request.user
    user.aboutme = request.POST.get('aboutme')
    user.save()
    if user.is_landlord:
        return redirect('/profiles/landlord/')
    else:
        return redirect('/profiles/')

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



def logout_view(request):
    logout(request)
    return redirect('/')  


