# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-09-21 04:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elephant', '0012_daangogoro'),
    ]

    operations = [
        migrations.CreateModel(
            name='daannarrowroadway',
            fields=[
                ('mapName', models.CharField(max_length=60)),
                ('mapLat', models.CharField(max_length=20)),
                ('mapLng', models.CharField(max_length=20)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('mapAddress', models.CharField(max_length=60)),
                ('mapcityID', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='daannoise',
            fields=[
                ('mapName', models.CharField(max_length=60)),
                ('mapLat', models.CharField(max_length=20)),
                ('mapLng', models.CharField(max_length=20)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('mapAddress', models.CharField(max_length=60)),
                ('mapcityID', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='daantemple',
            fields=[
                ('mapName', models.CharField(max_length=60)),
                ('mapLat', models.CharField(max_length=20)),
                ('mapLng', models.CharField(max_length=20)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('mapAddress', models.CharField(max_length=60)),
                ('mapcityID', models.CharField(max_length=20)),
            ],
        ),
    ]
