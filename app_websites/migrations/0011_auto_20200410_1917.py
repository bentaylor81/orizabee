# Generated by Django 3.0.3 on 2020-04-10 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_websites', '0010_auto_20200408_2132'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={},
        ),
        migrations.AlterField(
            model_name='partlist',
            name='category1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_websites.Category1'),
        ),
        migrations.AlterField(
            model_name='partlist',
            name='category2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_websites.Category2'),
        ),
    ]