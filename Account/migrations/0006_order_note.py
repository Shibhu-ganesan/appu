# Generated by Django 3.1 on 2020-09-06 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0005_auto_20200906_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.CharField(max_length=100, null=True),
        ),
    ]