# Generated by Django 3.0.3 on 2020-05-13 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_websites', '0017_auto_20200513_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='partlist',
            name='partlist_section',
            field=models.ManyToManyField(to='app_websites.PartListSection'),
        ),
    ]
