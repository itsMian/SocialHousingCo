from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.home, name="HomePage"),
    path('search/', views.search, name='search'),
]