# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-06 01:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0070_auto_20190506_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugs',
            name='status',
            field=models.CharField(choices=[('Fixed', 'Fixed'), ('Doing', 'Doing'), ('To do', 'To do')], default='To do', max_length=6),
        ),
        migrations.AlterField(
            model_name='bugs',
            name='type',
            field=models.CharField(choices=[('Worlds', 'Worlds'), ('Items', 'Items'), ('Base game', 'Base game'), ('Skills', 'Skills'), ('Quests', 'Quests')], default='Base game', max_length=10),
        ),
    ]
