from django.urls import path
from . import views

app_name = "app_shop"

urlpatterns = [
    path('home/', views.Home.as_view(), name="home"),
    path('pro-detials/<pk>/', views.ProductDetials.as_view(), name="product_detials"),
]