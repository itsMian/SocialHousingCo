from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
 
    path('', views.login_view, name='login_view'),
    path('newaccount/', views.rego, name='newaccount'),
  
    path('renter/home/', views.renter, name='renter'),
    path('landlord/home/', views.landlord, name='landlord'),
    
]