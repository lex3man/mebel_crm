# Generated by Django 4.0.1 on 2022-01-19 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0018_function_fund_function_inflow_fund_base'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=10)),
            ],
        ),
    ]
