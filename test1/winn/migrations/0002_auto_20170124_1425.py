# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winn', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conductor',
            name='total_c',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='conductor',
            name='d_id',
            field=models.CharField(max_length=26, primary_key=True, serialize=False),
        ),
    ]
