# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-07 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0090_auto_20190507_1647'),
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
            field=models.CharField(choices=[('Items', 'Items'), ('Quests', 'Quests'), ('Base game', 'Base game'), ('Skills', 'Skills'), ('Worlds', 'Worlds')], default='Base game', max_length=10),
        ),
    ]