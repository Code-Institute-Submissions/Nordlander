# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-20 18:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0011_auto_20190420_1839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='username',
        ),
    ]