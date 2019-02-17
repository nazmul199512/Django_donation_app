# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-01-28 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(max_length=100)),
                ('unit_of_Social_organ', models.CharField(max_length=100)),
                ('established_year', models.IntegerField()),
                ('organization_address', models.CharField(max_length=100)),
                ('contact_person', models.CharField(max_length=100)),
                ('registration_details', models.CharField(max_length=100)),
                ('fcra_details', models.CharField(max_length=100)),
                ('a_details', models.CharField(max_length=100)),
                ('g_details', models.CharField(max_length=100)),
                ('bank', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('account', models.CharField(max_length=100)),
                ('isfs', models.CharField(max_length=1000)),
            ],
        ),
    ]
