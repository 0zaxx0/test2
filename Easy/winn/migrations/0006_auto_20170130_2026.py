# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 20:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winn', '0005_condicionesref'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condicionesref',
            name='PeriodoCarga',
            field=models.CharField(max_length=60),
        ),
    ]
