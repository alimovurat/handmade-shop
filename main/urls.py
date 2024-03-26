from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.products_by_category, name='products_by_category'),
    path('technique/<str:technique>/', views.products_by_technique, name='products_by_technique'),
    path('one_product/<int:product_id>/', views.one_product, name='one_product'),
    path('one_product/<int:product_id>/add/', views.add_to_shopping_cart, name='add_to_shopping_cart'),
    path('delete_from_shopping_cart/<int:product_id>/', views.delete_from_shopping_cart, name='delete_from_shopping_cart'),
    path('clear_shopping_cart/', views.clear_shopping_cart, name='clear_shopping_cart'),
    path('shopping_cart/', views.shopping_cart, name='shopping_cart'),
    path('delivery/', views.delivery, name='delivery'),
    # path('profile/', views.profile, name='profile'),
]