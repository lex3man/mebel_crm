# Generated by Django 4.0.1 on 2022-01-19 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0020_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='function',
            name='fund',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='CRM.fund', verbose_name='Из фонда'),
        ),
        migrations.AlterField(
            model_name='function',
            name='inflow',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='CRM.inflow_base', verbose_name='или на основе'),
        ),
        migrations.AlterField(
            model_name='fund',
            name='base',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='CRM.inflow_base', verbose_name='Основа начисления'),
        ),
    ]
