
from django.urls import path
from . import views


urlpatterns = [
   path('add-to-cart/<pk>/',views.add_to_cart, name='add_to_cart'),
   path('cart/',views.cart_view, name='cart_view'),
   path('item-remove/<pk>/',views.item_remove, name='item_remove'),
   path('item-increase/<pk>/',views.item_increase, name='item_increase'),
   path('item-decrease/<pk>/',views.item_decrease, name='item_decrease'),
]
