# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-09-20 08:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elephant', '0003_delete_mapburglar'),
    ]

    operations = [
        migrations.CreateModel(
            name='mapburglar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mapName', models.CharField(max_length=60)),
                ('mapLat', models.CharField(max_length=20)),
                ('mapLng', models.CharField(max_length=20)),
                ('mapID', models.CharField(max_length=20)),
                ('mapAddr', models.CharField(max_length=60)),
                ('mapcityID', models.CharField(max_length=20)),
            ],
        ),
    ]
