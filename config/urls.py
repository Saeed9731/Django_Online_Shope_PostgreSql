from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('pages.urls')),
                  path('Products/', include('products.urls')),
                  path('accounts/', include('allauth.urls')),
                  path('cart/', include('cart.urls')),
                  path('order/', include('orders.urls')),

                  # Roseta (i18n)
                  path('rosetta/', include('rosetta.urls'))
              ] \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
