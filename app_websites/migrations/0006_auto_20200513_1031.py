# Generated by Django 3.0.3 on 2020-05-13 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_websites', '0005_auto_20200513_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='desc',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='part',
            name='link',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='part',
            name='part_diagram',
            field=models.ManyToManyField(blank=True, to='app_websites.PartDiagram'),
        ),
    ]
