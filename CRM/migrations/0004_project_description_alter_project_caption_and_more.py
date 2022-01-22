# Generated by Django 4.0.1 on 2022-01-12 09:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0003_project_additional_tools'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.CharField(default='', max_length=1000, verbose_name='Описание проекта'),
        ),
        migrations.AlterField(
            model_name='project',
            name='caption',
            field=models.CharField(max_length=200, verbose_name='Наименование проекта'),
        ),
        migrations.AlterField(
            model_name='project',
            name='construct',
            field=models.BooleanField(default=True, verbose_name='Сборка'),
        ),
        migrations.AlterField(
            model_name='project',
            name='designerless',
            field=models.BooleanField(default=False, verbose_name='Промо 10% (не дизайнерский)'),
        ),
        migrations.AlterField(
            model_name='project',
            name='discount',
            field=models.FloatField(default=0, verbose_name='Дополнительная скидка, %'),
        ),
        migrations.AlterField(
            model_name='project',
            name='map_price',
            field=models.FloatField(default=0, verbose_name='МРЦ'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(editable=False, max_length=200, verbose_name='Имя записи'),
        ),
        migrations.AlterField(
            model_name='project',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='project',
            name='shipping',
            field=models.BooleanField(default=True, verbose_name='Доставка'),
        ),
        migrations.AlterField(
            model_name='project',
            name='total_price',
            field=models.FloatField(default=0, verbose_name='Итоговая стоимость'),
        ),
        migrations.AlterField(
            model_name='tool',
            name='caption',
            field=models.CharField(max_length=200, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='tool',
            name='description',
            field=models.CharField(max_length=1000, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='tool',
            name='diler_price',
            field=models.FloatField(default=0, verbose_name='Закупочная стоимость'),
        ),
        migrations.AlterField(
            model_name='tool',
            name='name',
            field=models.CharField(editable=False, max_length=200),
        ),
        migrations.AlterField(
            model_name='tool',
            name='riental_price',
            field=models.FloatField(default=0, verbose_name='Итоговая стоимость'),
        ),
    ]