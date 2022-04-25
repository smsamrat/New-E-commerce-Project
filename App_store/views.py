from urllib import request
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Models
from .models import Category, Product

# Create your views here.

class Store(ListView):
    model = Product
    template_name = 'app_store/store.html'

class ProductDetails(DetailView,LoginRequiredMixin):
    model = Product
    template_name = "app_store/details_page.html"
