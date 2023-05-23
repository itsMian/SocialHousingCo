"""
URL configuration for SocialHousingCo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Database import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('', include("Home.urls")),
    path('listpage/', include("Listpage.urls")),
    path('admin/', admin.site.urls),
    path('myproperty/', views.showproperty),
    path('login/', include("Login.urls")),
     path('createaccount/', include("Createaccount.urls")),
     path('profiles/', include("Userprofile.urls")),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
