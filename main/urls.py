from django.urls import path
from . import views


urlpatterns = [
    path('', views.paintings, name='paintings'),
    path('stuffed_toys/', views.stuffed_toys, name='stuffed_toys'),
    path('brooches/', views.brooches, name='brooches'),
    path('product/', views.product, name='product'),
    path('shopping_cart/', views.shopping_cart, name='shopping_cart'),
]