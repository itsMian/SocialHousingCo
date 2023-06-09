from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.listview, name="listpage"),
    path("<int:id>/", views.PropertyDetailView.as_view(), name="detailspage"),
    path("createproperty/", views.createpropertypage, name="createpropertypage"),
    path("storeproperty/", views.storeProperty, name="storeproperty"),
    path("<int:id>/edit/", views.PropertyEditView.as_view(), name="editproperty"),
    path("<int:id>/updadeproperty/", views.updateProperty, name="updateproperty"),
    path("<int:id>/deleteproperty/", views.deleteProperty, name="deleteproperty"),
    path("search/", views.searchProperty, name='searchproperty'),
    path("sort/", views.sortProperty, name='sortproperty'),
    path("mapview/", views.mapview, name='mapview'),
]

