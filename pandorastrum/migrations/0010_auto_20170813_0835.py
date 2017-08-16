# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-13 02:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pandorastrum', '0009_auto_20170813_0830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamesmodelpage',
            name='game_title',
        ),
        migrations.AddField(
            model_name='gamesmodelpage',
            name='game_title',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='pandorastrum.GamesForModel'),
        ),
    ]
