# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-09-20 10:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elephant', '0006_auto_20170920_1819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mapburglar',
            name='mapcityID',
        ),
    ]
