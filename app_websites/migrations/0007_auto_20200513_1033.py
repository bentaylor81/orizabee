# Generated by Django 3.0.3 on 2020-05-13 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_websites', '0006_auto_20200513_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='part_diagram',
            field=models.ManyToManyField(blank=True, to='app_websites.PartListSection'),
        ),
    ]