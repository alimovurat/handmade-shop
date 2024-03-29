from django.contrib import admin
from django.urls import include, path
from app import settings
from django.conf.urls.static import static
from main.urls import urlpatterns as main_urls
from authentication.urls import urlpatterns as auth_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(main_urls)),
    path('', include(auth_urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
