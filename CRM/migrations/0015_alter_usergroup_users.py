# Generated by Django 4.0.1 on 2022-01-18 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0014_alter_user_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergroup',
            name='users',
            field=models.ManyToManyField(blank=True, to='CRM.User', verbose_name='Пользователи'),
        ),
    ]