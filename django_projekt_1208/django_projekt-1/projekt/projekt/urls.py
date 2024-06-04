"""
URL configuration for projekt project.

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
from django.urls import path
from . import views
from .views import kolegij_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('ja/', views.ja_view, name='ja'),
    path('kolegij/', views.kolegij_view, name='kolegij'),
    path('pocetna/', views.pocetna_view, name='pocetna'),
    path('kolegij/', kolegij_list, name='Kolegiji'),
    path('', views.login_view, name='login'),
    path('create_kolegij/', views.create_kolegij, name='create_kolegij'),
    path('create_obavijest/', views.create_obavijest, name='create_obavijest'),
    path('create_profesor/', views.create_profesor, name='create_profesor')

]
