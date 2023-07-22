# Generated by Django 4.0.2 on 2023-07-22 20:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_datetime_create_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='product',
            name='datetime_create',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 22, 20, 55, 41, 338912, tzinfo=utc), verbose_name='Date time created'),
        ),
    ]
