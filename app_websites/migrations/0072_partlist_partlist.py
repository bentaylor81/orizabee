# Generated by Django 3.0.3 on 2020-04-19 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_websites', '0071_auto_20200419_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='partlist',
            name='partlist',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]