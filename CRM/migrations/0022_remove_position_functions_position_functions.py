# Generated by Django 4.0.1 on 2022-01-19 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0021_alter_function_fund_alter_function_inflow_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='position',
            name='functions',
        ),
        migrations.AddField(
            model_name='position',
            name='functions',
            field=models.ManyToManyField(blank=True, default=None, to='CRM.Function', verbose_name='Функции'),
        ),
    ]
