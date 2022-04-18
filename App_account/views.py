from django.shortcuts import render,redirect,HttpResponseRedirect
from django.urls import reverse 
from django.contrib.auth import authenticate, login,logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm
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

def userlogin(request):
    form =AuthenticationForm()
    if request.method == "POST":
        form =AuthenticationForm(request,data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
            return redirect('store')
    return render(request,'app_account/login.html',context={'form':form})

def userlogout(request):
    logout(request)
    return redirect('login')