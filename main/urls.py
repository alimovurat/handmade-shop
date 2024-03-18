from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    # path('products', views.products, name='products'),
    path('category/<int:category_id>/', views.products_by_category, name='products_by_category'),
    # path('technique/<str:technique>/', views.products_by_technique, name='products_by_technique'),
    path('one_product/', views.one_product, name='one_product'),
    path('shopping_cart/', views.shopping_cart, name='shopping_cart'),
    path('delivery/', views.delivery, name='delivery'),
]