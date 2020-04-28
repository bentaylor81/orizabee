# Generated by Django 3.0.3 on 2020-04-17 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_websites', '0043_brand_small_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machine',
            name='start_year',
        ),
        migrations.AddField(
            model_name='machine',
            name='year_from',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='machine',
            name='year_to',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
    ]
