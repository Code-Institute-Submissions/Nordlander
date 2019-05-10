# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-10 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0095_auto_20190510_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='features',
            name='status',
            field=models.CharField(choices=[('Available', 'Available'), ('Doing', 'Doing'), ('To do', 'To do')], default='To do', max_length=14),
        ),
        migrations.AlterField(
            model_name='features',
            name='type',
            field=models.CharField(choices=[('Items', 'Items'), ('Quests', 'Quests'), ('Worlds', 'Worlds'), ('Skills', 'Skills')], default='Items', max_length=10),
        ),
    ]
