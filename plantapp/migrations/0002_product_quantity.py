# Generated by Django 4.2.3 on 2023-08-11 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]