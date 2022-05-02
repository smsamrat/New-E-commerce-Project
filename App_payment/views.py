from django.shortcuts import redirect, render
from App_order.models import Order,Cart
from App_account.models import Profile
from .models import BillignsAddress
from .forms import BillignsAddressForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#payment
import requests
from sslcommerz_python.payment import SSLCSession
from decimal import Decimal
import socket

# Create your views here.
@login_required
def checkout(request):
    save_address = BillignsAddress.objects.get_or_create(user=request.user)[0]

    form = BillignsAddressForm(instance=save_address)
    if request.method == 'POST':
        form = BillignsAddressForm(request.POST,instance=save_address)
        if form.is_valid():
            form.save()
            form = BillignsAddressForm(instance=save_address)
    # order_item = Cart.objects.filter(user=request.user, purchased=False)#aivbae dia jai
    order_qs = Order.objects.filter(user=request.user, orderd=False)
    order_item = order_qs[0].orderItems.all()
    order_total = order_qs[0].get_totals

    return render(request,'app_payment/checkout.html',context={'form':form,'order_item':order_item,
    'order_total':order_total,
    'save_address':save_address
    
    })

def payment(request):
    save_address = BillignsAddress.objects.get_or_create(user = request.user)
    if not save_address[0].is_fully_filled():
        messages.warning(request,'Please save the delivary address')
        return redirect('checkout')
        
    if not request.user.profile.is_fully_filled():
        messages.info(request,'Please Fill up your Profile')
        return redirect('custom_profile')
    return render(request,'app_payment/payment.html',context={})


