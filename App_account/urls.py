from django.contrib import admin
from django.urls import path
from App_account import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.userlogin, name='login'),
    path('logout/', views.userlogout, name='logout'),
    path('user-profile/', views.user_profile, name='user_profile'),
]