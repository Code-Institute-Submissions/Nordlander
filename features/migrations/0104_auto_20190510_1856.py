# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-10 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0103_auto_20190510_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='features',
            name='type',
            field=models.CharField(choices=[('Items', 'Items'), ('Quests', 'Quests'), ('Skills', 'Skills'), ('Worlds', 'Worlds')], default='Items', max_length=10),
        ),
    ]
