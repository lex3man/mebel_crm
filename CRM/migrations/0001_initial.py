# Generated by Django 4.0.1 on 2022-01-12 08:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now)),
                ('designerless', models.BooleanField(default=False)),
                ('discount', models.FloatField(default=0)),
                ('map_price', models.FloatField(default=0)),
                ('construct', models.BooleanField(default=True)),
                ('shipping', models.BooleanField(default=True)),
                ('total_price', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Tools',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('diler_price', models.FloatField(default=0)),
                ('riental_price', models.FloatField(default=0)),
            ],
        ),
    ]
