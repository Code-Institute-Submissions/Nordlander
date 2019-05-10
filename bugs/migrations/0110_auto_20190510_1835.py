# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-10 18:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0109_auto_20190510_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugs',
            name='status',
            field=models.CharField(choices=[('Doing', 'Doing'), ('Fixed', 'Fixed'), ('To do', 'To do')], default='To do', max_length=6),
        ),
        migrations.AlterField(
            model_name='bugs',
            name='type',
            field=models.CharField(choices=[('Worlds', 'Worlds'), ('Items', 'Items'), ('Base game', 'Base game'), ('Quests', 'Quests'), ('Skills', 'Skills')], default='Base game', max_length=10),
        ),
    ]
