# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-11 00:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0115_auto_20190511_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugs',
            name='status',
            field=models.CharField(choices=[('Fixed', 'Fixed'), ('To do', 'To do'), ('Doing', 'Doing')], default='To do', max_length=50),
        ),
        migrations.AlterField(
            model_name='bugs',
            name='type',
            field=models.CharField(choices=[('Skills', 'Skills'), ('Worlds', 'Worlds'), ('Base game', 'Base game'), ('Quests', 'Quests'), ('Items', 'Items')], default='Base game', max_length=50),
        ),
    ]
