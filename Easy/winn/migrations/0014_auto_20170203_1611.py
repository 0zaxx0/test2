# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 16:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winn', '0013_auto_20170203_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='condiciones',
            name='NumCarrerasEspecial',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='condiciones',
            name='ReferidoEspecial',
            field=models.CharField(default='', max_length=100),
        ),
    ]
