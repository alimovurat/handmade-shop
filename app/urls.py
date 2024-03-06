from django.contrib import admin
from django.urls import include, path
from main.urls import urlpatterns as main_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(main_urls))
]
