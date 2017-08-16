# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-15 21:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pandorastrum', '0019_gamesgallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamesgallery',
            name='related_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pandorastrum.GamesModel'),
        ),
    ]
