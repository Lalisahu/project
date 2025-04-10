"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from app import views  # Import the views from your app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Add this line to include the app's URL pattern
   
    path('about/', views.about, name='about'),  # Add this line to include the app's URL pattern
    path('contact/', views.contact, name='contact'),  # Add this line to include the app's URL pattern
    path('base/', views.base, name='base'),  # Add this line to include the app's URL pattern
    path('registen/', views.registen, name='registen'),  # Add this line to include the app's URL pattern
    path('registen_form/', views.registen_form, name='registen_form'),  # Add this line to include the app's URL pattern
  
]
