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
    print("Item:________________")
    print(item)
    cart_item = Cart.objects.get_or_create(item=item, user=request.user, purchased=False)
    print("Cart Item_______________________")
    print(cart_item)
    print(cart_item[0])
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        print("If order exit----------------------------")
        print(order)
        if order.orderitems.filter(item=item).exists():
            cart_item[0].quantity+=1
            cart_item[0].save()
            messages.info(request, "This item quantity was updated!")
            return redirect('app_shop:home')
        else:
            order.orderitems.add(cart_item[0])
            messages.info(request,"this item was added to your cart!")
            return redirect('app_shop:home')
    else:
        order = Order(user=request.user)
        order.save()
        order.orderitems.add(cart_item[0])
        messages.info(request, "this item was added to your cart!")
        return redirect('app_shop:home')