# Generated by Django 3.1 on 2020-08-17 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_order_products'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]