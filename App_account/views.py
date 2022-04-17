from urllib import request
from django.shortcuts import render
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.models import User
from .forms import CreateUserForm

# Create your views here.

def signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(data = request.POST)
        if form.is_valid():  
            form.save()
    return render(request,'app_account/signup.html',context={'form':form})