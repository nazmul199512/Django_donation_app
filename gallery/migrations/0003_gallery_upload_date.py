# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-01-30 18:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20190130_0150'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 30, 18, 1, 59, 554888, tzinfo=utc)),
        ),
    ]
