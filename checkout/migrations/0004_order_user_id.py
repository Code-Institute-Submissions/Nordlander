# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-06 01:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('checkout', '0003_orderlineitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user_id',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
