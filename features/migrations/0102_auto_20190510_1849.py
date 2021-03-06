# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-10 18:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0101_auto_20190510_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='features',
            name='status',
            field=models.CharField(choices=[('Doing', 'Doing'), ('To do', 'To do'), ('Available', 'Available')], default='To do', max_length=14),
        ),
        migrations.AlterField(
            model_name='features',
            name='type',
            field=models.CharField(choices=[('Quests', 'Quests'), ('Skills', 'Skills'), ('Worlds', 'Worlds'), ('Items', 'Items')], default='Items', max_length=10),
        ),
    ]
