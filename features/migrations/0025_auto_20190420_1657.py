# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-20 16:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0024_auto_20190420_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='features',
            name='status',
            field=models.CharField(choices=[('To do', 'To do'), ('Available', 'Available'), ('Doing', 'Doing')], default='To do', max_length=14),
        ),
    ]
