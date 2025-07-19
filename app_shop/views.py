from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Category
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


class Home(ListView):
    context_object_name = 'object_list'
    model = Product
    template_name = 'app_shop/home.html'


class ProductDetials(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'app_shop/product_details.html'