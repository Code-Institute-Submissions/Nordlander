# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-19 18:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20190419_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='bug_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bugs.Bugs'),
        ),
    ]
