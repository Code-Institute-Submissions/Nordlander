# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-17 23:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0009_auto_20190417_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugs',
            name='status',
            field=models.CharField(choices=[('FIXED', 'Fixed!'), ('TODO', 'To do'), ('DOING', 'Doing')], default='TODO', max_length=6),
        ),
    ]
