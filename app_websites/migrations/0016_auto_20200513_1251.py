# Generated by Django 3.0.3 on 2020-05-13 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_websites', '0015_auto_20200513_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='partlist_section',
            field=models.ManyToManyField(to='app_websites.PartListSection'),
        ),
    ]
