# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-19 01:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0003_auto_20180118_1815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='host_name',
            name='Project',
        ),
        migrations.RemoveField(
            model_name='publisher',
            name='package',
        ),
        migrations.DeleteModel(
            name='host_name',
        ),
        migrations.DeleteModel(
            name='package',
        ),
    ]
