from django.contrib import admin
from django.urls import path

from .views import contactView, successView, contactsView
from contact import views

app_name = 'contact'

urlpatterns = [
    path('contact_data', contactsView, name='contact_data'),
    path('contact', contactView, name='contact'),
    path('success', successView, name='success'),
]