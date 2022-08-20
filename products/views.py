from django.views import generic

from .models import Product


class ProductsListView(generic.ListView):
    # model = Product
    queryset = Product.objects.filter(active=True)
    template_name = 'product/product_list.html'
    context_object_name = 'products'


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'product/product_detail.html'
    context_object_name = 'product'
