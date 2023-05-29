from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Profiles
from register.models import User
from .forms import IncomeForm
from .choices import income_type_choices, pay_frequency_choices
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

def income(request):
    user = request.user
    user.income_type = request.POST.get('income_type')
    user.pay_frequency = request.POST.get('pay_frequency')
    user.amount_after_tax = request.POST.get('amount_after_tax')
    context = {
        'income_type_choices': income_type_choices,
        'pay_frequency_choices': pay_frequency_choices,
        'values': request.POST
    }        
    return render(request, 'income.html', context)

@csrf_protect
def update_income(request):
    if request.method == 'POST':
        user = request.user
        user.income_type = request.POST.get('income_type')
        user.pay_frequency = request.POST.get('pay_frequency')
        user.amount_after_tax = request.POST.get('amount_after_tax')
        user.save()
    return redirect('/profiles/')


def referal_letter(request):
    return render(request, 'referal-letter.html')



def logout_view(request):
    logout(request)
    return redirect('/')  


# def button_view(request):
#     # Set the session variable when the button is clicked.
#     if request.method == 'POST':
#         request.session['show_image'] = True
#     ...
#     return render(request, 'profile.html')

# def image_view(request):
#     context = {
#         'show_image': request.session.get('show_image', False)
#     }
#     # Make sure to delete the session variable after using it.
#     if 'show_image' in request.session:
#         del request.session['show_image']
#     return render(request, 'profile.html', context)