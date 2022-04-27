from django.shortcuts import render
from App_order.models import Order,Cart
from .models import BillignsAddress
from .forms import BillignsAddressForm
from django.contrib.auth.decorators import login_required
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

    return render(request,'app_payment/checkout.html',context={'form':form,'order_item':order_item,'order_total':order_total})


