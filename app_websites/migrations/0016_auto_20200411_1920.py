# Generated by Django 3.0.3 on 2020-04-11 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_websites', '0015_series'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand',
            old_name='brand_name',
            new_name='brand',
        ),
    ]
