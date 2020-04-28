# Generated by Django 3.0.3 on 2020-04-05 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_websites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('position', models.IntegerField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='category1',
            name='position',
            field=models.IntegerField(null=True),
        ),
    ]
