# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-21 12:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comments', '0016_auto_20190421_1251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='user_id',
        ),
        migrations.AddField(
            model_name='comments',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
