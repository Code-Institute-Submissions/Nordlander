# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-06 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0077_auto_20190506_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugs',
            name='status',
            field=models.CharField(choices=[('To do', 'To do'), ('Doing', 'Doing'), ('Fixed', 'Fixed')], default='To do', max_length=6),
        ),
        migrations.AlterField(
            model_name='bugs',
            name='type',
            field=models.CharField(choices=[('Worlds', 'Worlds'), ('Items', 'Items'), ('Quests', 'Quests'), ('Skills', 'Skills'), ('Base game', 'Base game')], default='Base game', max_length=10),
        ),
    ]
