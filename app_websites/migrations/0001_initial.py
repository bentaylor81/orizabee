# Generated by Django 3.0.3 on 2020-04-05 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(default='', max_length=200)),
                ('description', models.CharField(default='', max_length=200)),
                ('position', models.IntegerField(unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_edited', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('position', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PartList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(default='westwood', max_length=200)),
                ('category1', models.ForeignKey('Category1', on_delete=models.CASCADE, null=True)),
                ('machine_year', models.CharField(blank=True, max_length=200, null=True)),
                ('machine_model', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('list_url', models.CharField(default='url', max_length=200)),
            ],
        ),
    ]
