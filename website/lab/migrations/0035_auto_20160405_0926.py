# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-05 03:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0034_auto_20160405_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
