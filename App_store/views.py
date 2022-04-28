import imp
from urllib import request
from django.shortcuts import redirect, render
from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

# Models
from .models import Category, Product

# Create your views here.

def store(request):
    products = Product.objects.filter()
    return render(request,'app_store/store.html',context={'object_list':products})

def product_fetch_by_category(request, slug):
    if(Category.objects.filter(slug=slug)):
        products = Product.objects.filter(category__slug=slug)
        return render(request,'app_store/store.html',context={'object_list':products})
    else:
        messages.warning(request,'Product is not available')
        return redirect('store')

def product_details(request,cat_slug,prod_slug):
    if(Category.objects.filter(slug=cat_slug)):
        if(Product.objects.filter(slug=prod_slug)):
            products = Product.objects.filter(slug=prod_slug).first()
    return render(request,'app_store/details_page.html',context={'single_product':products})