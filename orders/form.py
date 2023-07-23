from django import forms

from .models import Order
from django.utils.translation import gettext_lazy as _


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone_number', 'State', 'city', 'address', 'postal_code', 'orders_note', ]
        widgets = {
            'orders_note': forms.Textarea(
                attrs={'rows': 3, 'placeholder': _('If you have any notes please enter here')}),
        }
