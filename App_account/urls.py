from django.contrib import admin
from django.urls import path
from App_account import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.userlogin, name='login'),
]