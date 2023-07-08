from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('Products/', include('products.urls')),
    path('accounts/', include('allauth.urls')),
    path('cart/', include('cart.urls')),

    # Roseta (i18n)
    path('rosetta/', include('rosetta.urls'))
]
