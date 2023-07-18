from django.contrib import admin

from .models import Product, Comment
from jalali_date.admin import ModelAdminJalaliMixin

class CommentInline(admin.TabularInline):
    model = Comment
    fields = ['author', 'body', 'stars', 'active', ]
    extra = 1


@admin.register(Product)
class ProductAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'price', 'active', 'reduction', 'price_reduction']

    inlines = [
        CommentInline,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'author', 'body', 'stars', 'active', ]
