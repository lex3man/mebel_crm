# Generated by Django 4.0.1 on 2022-01-19 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0015_alter_usergroup_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='up_shipping',
            field=models.BooleanField(default=True, verbose_name='Подъем'),
        ),
    ]