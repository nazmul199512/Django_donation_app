# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-01-30 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20190131_0239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(blank=True, upload_to='gallery'),
        ),
    ]
