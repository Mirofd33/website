# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-18 10:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0002_auto_20171219_2109'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jenkins_source',
            options={'verbose_name': 'jenkins\u914d\u7f6e', 'verbose_name_plural': 'jenkins\u914d\u7f6e'},
        ),
        migrations.AddField(
            model_name='host',
            name='escode',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='\u5feb\u901f\u670d\u52a1\u4ee3\u7801'),
        ),
        migrations.AddField(
            model_name='host',
            name='housecode',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='\u673a\u623f\u7f16\u53f7'),
        ),
        migrations.AddField(
            model_name='host',
            name='server_id',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='\u670d\u52a1\u5668ID'),
        ),
        migrations.AddField(
            model_name='host',
            name='uplink',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='\u4e0a\u8054\u7aef\u53e3'),
        ),
        migrations.AlterField(
            model_name='host',
            name='re_per',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='\u8d1f\u8d23\u4eba'),
        ),
    ]
