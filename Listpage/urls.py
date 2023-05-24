from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.listview, name="listpage"),
    path("<int:id>/", views.PropertyDetailView.as_view(), name="detailspage"),
    path("createproperty/", views.createpropertypage, name="createpropertypage"),
    path("modalpage/", views.modalpage, name="modalpage"),
    path("storeproperty/", views.storeProperty, name="storeproperty"),
    path("<int:id>/edit/", views.PropertyEditView.as_view(), name="editproperty"),
    path("<int:id>/updadeproperty/", views.updateProperty, name="updateproperty"),
    path("<int:id>/deleteproperty/", views.deleteProperty, name="deleteproperty"),
]

