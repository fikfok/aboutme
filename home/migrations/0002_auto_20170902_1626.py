# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='personages',
            field=models.ManyToManyField(blank=True, null=True, to='home.Personages', verbose_name='Персонажи'),
        ),
    ]
