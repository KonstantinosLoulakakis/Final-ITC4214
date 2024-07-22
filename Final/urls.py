from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
# from django.conf import settings

#the motherships urls for full navigation within the site

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('index.urls')),
    path('', include('index.urls')),
    path('products/', include('products.urls')),
    path('account/', include('account.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
