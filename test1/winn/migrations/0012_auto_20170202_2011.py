# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 20:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winn', '0011_auto_20170202_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicobienvenida',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
