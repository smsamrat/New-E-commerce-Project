from dataclasses import fields
from django import forms
from .models import User  
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields=('first_name','last_name','email','password1','password2')