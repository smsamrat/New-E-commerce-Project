
from django.urls import path
from . import views


urlpatterns = [
   path('checkout/',views.checkout, name="checkout"),
   path('pay/',views.payment, name="payment"),
]
