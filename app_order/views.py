from django.shortcuts import render, get_object_or_404, redirect

#messages
from  django.contrib import messages
#athentication 
from django.contrib.auth.decorators import login_required
#models 
from .models import Cart, Order
from app_shop.models import Product


# Create your views here.

@login_required
def add_to_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_item = Cart.objects.get_or_create(item=item, user=request.user, purchased=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item[0].quantity += 1
            order_item.save()
            messages.info(request, "this Item quantity was updated!")
            return redirect("app_shop:home")
        else:
            order.orderitems.add(order_item[0])
            messages.info(request, "This item was added to your cart!")
            return redirect("app_shop:home")

    else:
        order = Order(user=request.user)
        order.save()
        order.orderitems.add(order_item[0])
        messages.info(request, 'this item was added to your cart.')
        return redirect('app_shop:home')