from django import template

register = template.Library()

@register.filter
def price_reduction(price,reduction=0):
    return price - reduction