# Generated by Django 3.0.3 on 2020-04-17 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_websites', '0040_auto_20200417_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='start_year',
            field=models.IntegerField(blank=True, choices=[(1980, 'Y1980'), (1981, 'Y1981')], default='1980', null=True),
        ),
    ]
