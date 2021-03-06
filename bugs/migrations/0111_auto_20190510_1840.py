# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-10 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0110_auto_20190510_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugs',
            name='status',
            field=models.CharField(choices=[('Doing', 'Doing'), ('To do', 'To do'), ('Fixed', 'Fixed')], default='To do', max_length=6),
        ),
        migrations.AlterField(
            model_name='bugs',
            name='type',
            field=models.CharField(choices=[('Base game', 'Base game'), ('Quests', 'Quests'), ('Skills', 'Skills'), ('Worlds', 'Worlds'), ('Items', 'Items')], default='Base game', max_length=10),
        ),
    ]
