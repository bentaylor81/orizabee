# Generated by Django 3.0.3 on 2020-04-15 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_websites', '0032_auto_20200413_2005'),
    ]

    operations = [
        migrations.RenameField(
            model_name='model',
            old_name='model_path',
            new_name='path',
        ),
        migrations.RenameField(
            model_name='series',
            old_name='series_path',
            new_name='path',
        ),
    ]