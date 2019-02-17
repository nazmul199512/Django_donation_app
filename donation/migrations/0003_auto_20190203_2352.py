# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-02-03 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0002_volunteer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteerregistration',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='volunteerregistration',
            name='city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='volunteerregistration',
            name='country',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='volunteerregistration',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='volunteerregistration',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='volunteerregistration',
            name='phone',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='volunteerregistration',
            name='zip_pin_code',
            field=models.CharField(max_length=100),
        ),
    ]
