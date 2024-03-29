from products.models import Product
from django.contrib import messages
from django.utils.translation import gettext as _


class Cart:
    def __init__(self, request):
        """
        Initialize the cart
        """
        self.request = request
        self.session = request.session

        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}

        self.cart = cart

    def remove(self, product):
        """
        Remove product of the cart id
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            messages.success(self.request, _(f'{product.title} successfully deleted from cart'))
            self.save()

    def add(self, product, quantity=1, replace_current_quantity=False):
        """
        Add the specified product to the cart if it exits
        """
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0}
        if replace_current_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        messages.success(self.request, _('{} successfully added to cart'.format(product.title)))
        self.save()

    def save(self):
        """
        Mark session ad modified to save changes
        """
        self.session.modified = True

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product_obj'] = product

        for item in cart.values():
            if item['product_obj'].reduction:
                item['total_price'] = (item['product_obj'].price - item['product_obj'].price_reduction) * item[
                    'quantity']
            else:
                item['total_price'] = item['product_obj'].price * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session['cart']
        messages.success(self.request, _('All product successfully clear'))
        self.save()

    def get_total_price(self):
        i = 0
        for item in self.cart.values():
            if item['product_obj'].reduction:
                item_reduction_price_total = (item['product_obj'].price - item['product_obj'].price_reduction) * item[
                    'quantity']
                item_price_total = 0
            else:
                item_price_total = item['product_obj'].price * item['quantity']
                item_reduction_price_total = 0

            total_price = item_reduction_price_total + item_price_total
            i += total_price
        return i

    def get_total_price_without_reduction(self):
        return sum(item['product_obj'].price * item['quantity'] for item in self.cart.values())

    def get_total_quantity(self):
        return self.__len__()

    def get_total_reduction(self):
        i = 0
        for item in self.cart.values():
            if item['product_obj'].reduction:
                item_reduction = item['product_obj'].price_reduction * item['quantity']
            else:
                item_reduction = 0

            total_price = item_reduction
            i += total_price
        return i
