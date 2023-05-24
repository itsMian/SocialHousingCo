from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'login.html')









@csrf_protect
def signin(request):
    if request.method == 'POST':
        email = request.POST['Email']
        password = request.POST['password']
        
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('/profiles')
        else:
            messages.info(request, 'Invalid username or password')
            return redirect("/login")  # Add the return statement here
    else:
        return render(request, 'index.html')
