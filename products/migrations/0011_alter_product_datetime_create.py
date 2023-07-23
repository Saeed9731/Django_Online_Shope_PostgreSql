# Generated by Django 4.0.2 on 2023-07-23 16:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_product_datetime_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='datetime_create',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 23, 16, 30, 30, 184560, tzinfo=utc), verbose_name='Date time created'),
        ),
    ]
