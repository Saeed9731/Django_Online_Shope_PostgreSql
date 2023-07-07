class Cart:
    def __int__(self, request):
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
        if product_id  in self.cart:
            del self.cart[product_id]
            self.save()

    def add(self, product, quantity=1):
        """
        Add the specified product to the cart if it exits
        """
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': quantity}
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        """
        Mark session ad modified to save changes
        """
        self.session.modified = True
