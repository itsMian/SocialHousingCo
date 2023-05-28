from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("", views.index, name="profiles"),
    path("landlord/", views.land, name="landlord"),
    
    path("personal-details/", views.personal, name="personal"),
    path("about-me/", views.aboutme, name="aboutme"),
    path("identity-documents/", views.identity, name="identity"),
    path('income/', views.income_create, name='income'),
    path("referal-letter/", views.referal_letter, name="referal"),
     path('logout/', views.logout_view, name='logout'),
]