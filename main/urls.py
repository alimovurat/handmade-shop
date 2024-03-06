from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('product/', views.product, name='product'),
    path('shopping_cart/', views.shopping_cart, name='shopping_cart'),
]