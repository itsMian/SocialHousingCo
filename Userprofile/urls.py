from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("", views.index, name="profiles"),
    path("landlord/", views.land, name="land"),
    path("personal-details/", views.personal, name="personal"),
    path("updade-details/", views.update_details, name="updatedetails"),
    
    path("about-me/", views.aboutme, name="aboutme"),
    path("update-aboutme/", views.update_aboutme, name="updateaboutme"),

    path("identity-documents/", views.identity, name="identity"),
    path("updade-identity/", views.update_identity, name="updateidentity"),

    path('income/', views.income, name='income'),
    path('update-income/', views.update_income, name='updateincome'),

    path("referal-letter/", views.referal_letter, name="referal"),
    path("update-referal-letter/", views.update_referal_letter, name="updatereferalletter"),

     path('logout/', views.logout_view, name='logout'),

    #  path('button/', views.button_view, name='button'),
    # path('image/', views.image_view, name='image'),
]