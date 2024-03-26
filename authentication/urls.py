from django.urls import include, path
from . import views


urlpatterns = [
    path('auth/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('profile/info/', views.profile_info, name='profile_info'),
    path('profile/address/', views.profile_address, name='profile_address'),
    path('profile/orders/', views.profile_orders, name='profile_orders')
]