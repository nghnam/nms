# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-07 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='time_avg',
            field=models.CharField(blank=True, default='99', max_length=255),
        ),
    ]