
from django.contrib import admin
from django.urls import path
from App_store import views

urlpatterns = [
    path('', views.Store.as_view(), name='store'),
]
