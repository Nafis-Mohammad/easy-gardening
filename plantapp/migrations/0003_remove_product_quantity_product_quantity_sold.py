# Generated by Django 4.2.3 on 2023-08-11 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantapp', '0002_product_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
        migrations.AddField(
            model_name='product',
            name='quantity_sold',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
