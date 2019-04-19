# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-19 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0015_auto_20190419_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='features',
            name='status',
            field=models.CharField(choices=[('To do', 'To do'), ('Doing', 'Doing'), ('Available', 'Available')], default='To do', max_length=14),
        ),
    ]
