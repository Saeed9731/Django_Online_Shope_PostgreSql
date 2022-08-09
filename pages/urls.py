from django.urls import path, include

from .views import HomePageView, AboutUsPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('\aboutus', AboutUsPageView.as_view(), name='about_us'),
]
