# Generated by Django 3.0.3 on 2020-05-13 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_websites', '0003_partlistsection'),
    ]

    operations = [
        migrations.AddField(
            model_name='partlistsection',
            name='sort_order',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
    ]
