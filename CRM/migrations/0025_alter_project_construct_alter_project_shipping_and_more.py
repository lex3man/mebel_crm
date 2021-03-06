# Generated by Django 4.0.1 on 2022-01-29 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0024_resource_r_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='construct',
            field=models.BooleanField(default=False, verbose_name='Сборка'),
        ),
        migrations.AlterField(
            model_name='project',
            name='shipping',
            field=models.BooleanField(default=False, verbose_name='Доставка'),
        ),
        migrations.AlterField(
            model_name='project',
            name='up_shipping',
            field=models.BooleanField(default=False, verbose_name='Подъем'),
        ),
    ]
