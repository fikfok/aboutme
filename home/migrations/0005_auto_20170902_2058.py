# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20170902_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cities',
            name='description',
            field=models.TextField(verbose_name='Описание города'),
        ),
        migrations.AlterField(
            model_name='cities',
            name='photo',
            field=models.CharField(max_length=100, verbose_name='Фотография города'),
        ),
    ]
