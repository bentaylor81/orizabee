# Generated by Django 3.0.3 on 2020-04-22 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_websites', '0094_auto_20200422_2226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machine',
            name='to_year',
        ),
    ]
