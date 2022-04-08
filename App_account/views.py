from urllib import request
from django.shortcuts import render

# Create your views here.

def signup(request):
    return render(request,'app_account/signup.html')