
from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [
    path('', views.index,name= 'index'),# home page
    path('home', views.home,name= 'home'),
    path('login', views.login,name= 'login'), 
    path('registration', views.registration,name= 'registration'),
    path('contactus', views.contactus,name= 'contactus'),
    path('aboutus', views.aboutus,name= 'aboutus')
]
