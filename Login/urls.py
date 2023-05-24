from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="login"),
   path("signin/", views.signin, name="signin")
]


