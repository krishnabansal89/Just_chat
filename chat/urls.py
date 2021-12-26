from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.hello , name = 'hello'),
    path('login/',views.login),
    path('login-up/',views.loginup),
    path('sign-up/',views.sign)
]
