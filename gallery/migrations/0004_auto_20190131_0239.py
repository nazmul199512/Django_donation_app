# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-01-30 20:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_gallery_upload_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(blank=True, max_length=5, upload_to='gallery'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='upload_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
