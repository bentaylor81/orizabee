# Generated by Django 3.0.3 on 2020-04-18 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_websites', '0058_auto_20200418_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='partlist_temp',
            name='desc',
            field=models.CharField(default='url', max_length=2000),
        ),
    ]