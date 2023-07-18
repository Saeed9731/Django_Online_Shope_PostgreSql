from django.db import models

from django.utils import timezone
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField


class Product(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=150)
    # description = models.TextField(verbose_name=_('Description'))
    description = RichTextField()
    price = models.PositiveIntegerField(verbose_name=_('Price'), default=0)
    active = models.BooleanField(default=True)
    image = models.ImageField(verbose_name=_('Product image'), upload_to='product/product_cover/', blank=True)

    datetime_create = models.DateTimeField(default=timezone.now(), verbose_name=_('Date time created'))
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Detail', args=[self.pk])


class ActiveCommentManger(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentManger, self).get_queryset().filter(active=True)


class Comment(models.Model):
    PRODUCT_STARS = [
        ('1', _('Very Bad')),
        ('2', _('Bad')),
        ('3', _('Normal')),
        ('4', _('Good')),
        ('5', _('Perfect')),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='comments author',
    )
    body = models.TextField(verbose_name=_('Comment Text'))
    stars = models.CharField(max_length=10, choices=PRODUCT_STARS, verbose_name=_('What are your score'))

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now_add=True)

    active = models.BooleanField(default=True)

    # Manger
    object = models.Manager()
    active_comment_mager = ActiveCommentManger

    def get_absolute_url(self):
        return reverse('Detail', args=[self.product.id])
