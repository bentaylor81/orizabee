# Generated by Django 3.0.3 on 2020-04-17 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_websites', '0038_machine_start_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='start_year',
            field=models.IntegerField(blank=True, choices=[('1980', '1980'), ('1981', '1981'), ('1982', '1982'), ('1983', '1983'), ('1984', '1984'), ('1985', '1985'), ('1986', '1986'), ('1987', '1987'), ('1988', '1988'), ('1989', '1989')], default='1980', null=True),
        ),
    ]
