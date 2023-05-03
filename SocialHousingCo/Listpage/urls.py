from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="listpage"),
    path("detailspage/", views.detailspage, name="detailspage"),
]