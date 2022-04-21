from django.shortcuts import render,redirect,HttpResponseRedirect
from django.urls import reverse 
from django.contrib.auth import authenticate, login,logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .forms import CreateUserForm,UpdateProfile,ProfileForm
from .models import Profile

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

def user_profile(request):
    return render(request,'app_account/profile.html',context={}) 
def edit_profile(request):
    form = UpdateProfile(instance=request.user)
    if request.method == 'POST':
        form = UpdateProfile(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
        form = UpdateProfile(instance=request.user)
    return render(request,'app_account/edit_profile.html',context={'form':form}) 

def custom_profile(request):
    return render(request,'app_account/custom_change_pro.html',context={}) 
    
def change_profile(request):
    profile = Profile.objects.get(user =request.user)
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('custom_profile')
        form = ProfileForm(instance=profile)
    return render(request,'app_account/change_profile.html',context={'form':form}) 