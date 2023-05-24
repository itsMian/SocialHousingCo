from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="createaccount"),
  
      path("register/", views.register, name="register"),
      path("setupprofile/", views.setupprofile.as_view(), name="setupprofile"),
    

]



