# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-04 06:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0025_auto_20160404_0534'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='display_priority',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='peopletype',
            name='count_in_one_row',
            field=models.IntegerField(choices=[(1, '4 in a row'), (2, '6 in a row')], default=2),
        ),
    ]
