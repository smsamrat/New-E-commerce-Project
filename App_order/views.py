from django.shortcuts import render, get_object_or_404, redirect
from App_store.models import Product
from .models import Cart,Order
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required
def add_to_cart(request,pk):
    item = get_object_or_404(Product, pk=pk)
    order_item = Cart.objects.get_or_create(item=item,user=request.user, purchased=False)
    order_qs = Order.objects.filter(user=request.user, orderd = False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderItems.filter(item=item).exists():
            order_item[0].quantity += 1
            order_item[0].save()
            messages.success(request,'Update Product To Cart Successfully')
            return redirect('store')
        else:
            order.orderItems.add(order_item[0])
            messages.info(request,'This Product was Added To Cart')
            return redirect('store')
    else:
        order = Order(user=request.user)
        order.save()
        order.orderItems.add(order_item[0])
        messages.success(request,'Add Product To Cart Successfully')
        return redirect('store')

@login_required
def cart_view(request):
    carts = Cart.objects.filter(user=request.user, purchased=False)
    orders = Order.objects.filter(user=request.user, orderd=False)
    if carts.exists() and orders.exists():
        order = orders[0]
        return render(request,'app_order/cart.html',context={'carts':carts,'order':order})
    else:
        messages.warning(request,"You don't have any item in your cart")
        return redirect('store')
        
@login_required
def item_remove(request,pk):
    item = get_object_or_404(Product,pk=pk)
    order_qs = Order.objects.filter(user= request.user, orderd=False)
    if order_qs.exists():
        order =order_qs[0]
        if order.orderItems.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item,user= request.user, purchased=False)[0]
            order.orderItems.remove(order_item)
            order_item.delete()
            messages.warning(request,'Your item removed from cart')
            return redirect('cart_view')
        else:
            messages.warning(request,'your item was not in cart')
            return redirect('store')
    else:
        messages.warning(request,'your item was not in order')
        return redirect('store')
