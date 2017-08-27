# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pandorastrum', '0012_auto_20170827_0841'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamelore',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='gamegenre',
            name='game_genre',
            field=models.CharField(choices=[('SIMULATION', 'Simulation'), ('MMO', 'Mmo'), ('ACTION', 'Action'), ('2D', '2D'), ('3RD PERSON', '3rd Person'), ('RPG', 'Rpg'), ('PUZZLE', 'Puzzle'), ('PLATFORMER', 'Platformer'), ('BEAT EM UP', 'Beat em up'), ('ARCADE', 'Arcade'), ('INFINITE RUNNER', 'Infinite Runner'), ('STRATEGY', 'Strategy'), ('SPORTS', 'Sports'), ('FPS', 'Fps'), ('MOBA', 'Moba'), ('RACING', 'Racing'), ('ADVENTURE', 'Adventure'), ('SPACE', 'Space'), ('---', '---'), ('3D', '3d'), ('HACK N SLASH', 'Hack n slash'), ('SHOOTING', 'Shooting'), ('TRIVIA', 'Trivia')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='portfoliomodel',
            name='category_type',
            field=models.CharField(choices=[('EXPERIMENTAL', 'Experimental'), ('CONCEPT', 'Concept'), ('3D', '3d'), ('UNITY', 'Unity'), ('UNREAL', 'Unreal')], max_length=12),
        ),
    ]
