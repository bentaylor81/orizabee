# Generated by Django 3.0.3 on 2020-04-13 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_websites', '0024_auto_20200412_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='description',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
