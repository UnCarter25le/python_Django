# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-09-21 02:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elephant', '0010_auto_20170921_1031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='daanpets',
            old_name='mapAddr',
            new_name='mapAddress',
        ),
    ]