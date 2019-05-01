# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-28 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0046_auto_20190428_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='features',
            name='status',
            field=models.CharField(choices=[('Doing', 'Doing'), ('To do', 'To do'), ('Available', 'Available')], default='To do', max_length=14),
        ),
        migrations.AlterField(
            model_name='features',
            name='type',
            field=models.CharField(choices=[('Skills', 'Skills'), ('Items', 'Item'), ('Worlds', 'World'), ('Quests', 'Quests')], default='Items', max_length=6),
        ),
    ]