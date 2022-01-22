# Generated by Django 4.0.1 on 2022-01-12 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0004_project_description_alter_project_caption_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='QType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование типа')),
                ('code', models.CharField(max_length=10, verbose_name='Код типа')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование вопроса')),
                ('text', models.CharField(max_length=1000, verbose_name='Текст вопроса')),
            ],
        ),
        migrations.CreateModel(
            name='Wizard_step',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование шага')),
                ('title', models.CharField(max_length=500, verbose_name='Заголовок')),
                ('descriptor', models.CharField(max_length=1500, verbose_name='Дескриптор')),
                ('order', models.IntegerField(default=1, verbose_name='Порядковый номер')),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(editable=False, max_length=200),
        ),
    ]