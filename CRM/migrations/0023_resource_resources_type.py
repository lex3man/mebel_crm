# Generated by Django 4.0.1 on 2022-01-28 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0022_remove_position_functions_position_functions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=50, verbose_name='Наименование')),
                ('dimention', models.CharField(max_length=20, verbose_name='Единицы измерения')),
                ('price', models.FloatField(default=0, verbose_name='Цена за единицу')),
            ],
        ),
        migrations.CreateModel(
            name='Resources_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=50, verbose_name='Наименование')),
            ],
        ),
    ]
