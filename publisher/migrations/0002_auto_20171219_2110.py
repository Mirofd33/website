# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-19 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='version',
            name='lastbuildinfo',
        ),
        migrations.AddField(
            model_name='version',
            name='bagName',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='\u5305\u540d'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name_en',
            field=models.CharField(max_length=100, verbose_name='\u82f1\u6587\u540d'),
        ),
    ]
