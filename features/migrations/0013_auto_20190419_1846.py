# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-19 18:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0012_auto_20190419_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='features',
            name='type',
            field=models.CharField(choices=[('Worlds', 'World'), ('Items', 'Item'), ('Quests', 'Quests'), ('Skills', 'Skills')], default='Items', max_length=6),
        ),
    ]
