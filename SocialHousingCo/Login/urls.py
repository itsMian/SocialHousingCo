from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="login"),
   path("landlordlogin/", views.landlordlogin, name="landlordlogin"),

]


