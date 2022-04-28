
from django.contrib import admin
from django.urls import path
from App_store import views

urlpatterns = [
    path('', views.Store.as_view(), name='store'),
    path('details/<pk>/', views.ProductDetails.as_view(), name='details_page'),
    path('cetegory/<str:slug>/',views.product_fetch_by_category, name='category')
]
