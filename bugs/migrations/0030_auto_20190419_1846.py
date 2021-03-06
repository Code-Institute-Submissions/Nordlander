# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-19 18:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0029_auto_20190419_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugs',
            name='status',
            field=models.CharField(choices=[('To do', 'To do'), ('Fixed', 'Fixed'), ('Doing', 'Doing')], default='To do', max_length=6),
        ),
        migrations.AlterField(
            model_name='bugs',
            name='type',
            field=models.CharField(choices=[('Worlds', 'Worlds'), ('Items', 'Items'), ('Quests', 'Quests'), ('Skills', 'Skills'), ('Base game', 'Base game')], default='Base game', max_length=10),
        ),
    ]
