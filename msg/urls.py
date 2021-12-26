from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.test , name = 'hello'),
    path('data/',views.data),
    path('contact/',views.contact),
    path('click/',views.click),
    path('search/',views.search),
    path('make_contact/',views.make_contact)
]