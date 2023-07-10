from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact')
]
