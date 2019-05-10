# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-10 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0088_auto_20190507_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='features',
            name='type',
            field=models.CharField(choices=[('Items', 'Items'), ('Skills', 'Skills'), ('Worlds', 'Worlds'), ('Quests', 'Quests')], default='Items', max_length=6),
        ),
    ]
