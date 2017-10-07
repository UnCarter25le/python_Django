# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-09-21 02:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elephant', '0009_auto_20170920_1921'),
    ]

    operations = [
        migrations.CreateModel(
            name='daanpets',
            fields=[
                ('mapName', models.CharField(max_length=60)),
                ('mapLat', models.CharField(max_length=20)),
                ('mapLng', models.CharField(max_length=20)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('mapAddr', models.CharField(max_length=60)),
                ('mapcityID', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='daanburglar',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]