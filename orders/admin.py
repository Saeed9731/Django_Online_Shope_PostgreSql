from django.contrib import admin

from .models import Order, OderItem
from jalali_date.admin import ModelAdminJalaliMixin


class OderItemInline(admin.TabularInline):
    model = OderItem
    fields = ['order', 'product', 'quantity', 'price', ]
    extra = 1


@admin.register(Order)
class OrderAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'phone_number', 'datetime_create', 'is_paid', ]

    inlines = [
        OderItemInline,
    ]


@admin.register(OderItem)
class OderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price', ]
