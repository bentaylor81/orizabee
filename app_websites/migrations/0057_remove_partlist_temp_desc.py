# Generated by Django 3.0.3 on 2020-04-18 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_websites', '0056_auto_20200418_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partlist_temp',
            name='desc',
        ),
    ]
