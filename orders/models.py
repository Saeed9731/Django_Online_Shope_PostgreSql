from django.db import models
from django.conf import settings

from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_paid = models.BooleanField(_('is paid'), default=False)

    first_name = models.CharField(_('first name'), max_length=150)
    last_name = models.CharField(_('last name'), max_length=150)
    phone_number = models.CharField(_('phone number'), max_length=15)

    State = models.CharField(_('state'), max_length=15)
    city = models.CharField(_('city'), max_length=15)
    address = models.TextField(_('address'))
    postal_code = models.CharField(_('postal code'), max_length=15)
    orders_note = models.CharField(_('oder note'), max_length=700, blank=True)
    Email = models.EmailField(_('Email'), max_length=700, blank=True)

    datetime_create = models.DateTimeField(_('Date time created'), auto_now=True)
    datetime_modified = models.DateTimeField(_('Date time modified'), auto_now=True)

    def __str__(self):
        return f'Order {self.id}'


class OderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='item')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'OrdrItem {self.id}:  {self.product} X {self.quantity} (price:{self.price})'
