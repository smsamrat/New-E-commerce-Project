
from django.urls import path
from . import views


urlpatterns = [
   path('add-to-cart/<pk>/',views.add_to_cart, name='add_to_cart'),
   path('cart/',views.cart_view, name='cart_view'),
]
