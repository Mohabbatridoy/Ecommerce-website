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
def Add_to_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)

    #Get or Create a Cart object with clicked item
    cart_item = Cart.objects.get_or_create(item=item, user=request.user, purchased=False)

    #checking whether this user has a inactive order
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.exists():
            cart_item[0].quantity += 1
            cart_item.save()
            messages.info(request, "This item quantity was updated!")
            return redirect('app_shop:home')
        else:
            order.orderitems.add(cart_item[0])
            messages.info(request, "This item was added to your cart!")
            return redirect('app_shop:home')
    else:
        order = Order(user=request.user)
        order.save()
        order.orderitems.add(cart_item[0])
        messages.info(request, "This item was added to your cart!")
        return redirect('app-shop:home')
    
@login_required
def cart_view(request):
    carts = Cart.objects.filter(user=request.user, purchased=False)
    orders = Order.objects.filter(user=request.user, ordered=False)
    if carts.exists() and orders.exists():
        order = orders[0]
        return render(request, 'app_order/cart.html', context={'carts':carts,'order':order})
    else:
        messages.warning(request, "You don't have any item in your cart!")
        return redirect('app_shop:home')