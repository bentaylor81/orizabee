# Generated by Django 3.0.3 on 2020-04-11 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_websites', '0014_category1_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.CharField(max_length=200)),
            ],
        ),
    ]