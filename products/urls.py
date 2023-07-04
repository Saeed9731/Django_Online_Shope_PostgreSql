from django.urls import path

from .views import ProductsListView, ProductDetailView, CommentCreateView

urlpatterns = [
    path('', ProductsListView.as_view(), name='Product'),
    path('<int:pk>/', ProductDetailView.as_view(), name='Detail'),
    path('comment/<int:product_id>/', CommentCreateView.as_view(), name='comment_create'),
]
