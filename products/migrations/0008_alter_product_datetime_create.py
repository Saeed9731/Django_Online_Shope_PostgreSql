# Generated by Django 4.0.2 on 2023-07-23 10:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_product_active_alter_product_datetime_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='datetime_create',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 23, 10, 30, 5, 180369, tzinfo=utc), verbose_name='Date time created'),
        ),
    ]