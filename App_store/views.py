from urllib import request
from django.shortcuts import render

# Create your views here.

def store(request):
    return render(request,'app_store/store.html')
