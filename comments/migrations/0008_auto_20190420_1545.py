# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-20 15:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0007_auto_20190420_0223'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='likes',
            new_name='upvotes',
        ),
    ]
