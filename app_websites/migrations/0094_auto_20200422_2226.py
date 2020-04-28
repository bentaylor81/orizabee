# Generated by Django 3.0.3 on 2020-04-22 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_websites', '0093_auto_20200422_2224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machine',
            name='part',
        ),
        migrations.AddField(
            model_name='part',
            name='machine',
            field=models.ManyToManyField(blank=True, to='app_websites.Machine'),
        ),
    ]