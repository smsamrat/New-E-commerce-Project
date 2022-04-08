from django.contrib import admin
from django.urls import path
from App_account import views

urlpatterns = [
    path('', views.signup, name='signup'),
]