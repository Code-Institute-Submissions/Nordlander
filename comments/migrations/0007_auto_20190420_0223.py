# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-20 02:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0006_auto_20190420_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
