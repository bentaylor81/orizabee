# Generated by Django 3.0.3 on 2020-04-08 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_websites', '0004_auto_20200408_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='sort_order',
            field=models.IntegerField(default='0', null=True),
        ),
    ]