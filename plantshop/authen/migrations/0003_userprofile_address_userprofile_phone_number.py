# Generated by Django 4.2.3 on 2023-07-28 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0002_userprofile_delete_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
