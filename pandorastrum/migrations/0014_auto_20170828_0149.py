# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 19:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pandorastrum', '0013_auto_20170827_1252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutmodel',
            old_name='op_email',
            new_name='operation_email',
        ),
        migrations.RenameField(
            model_name='aboutmodel',
            old_name='pro_email',
            new_name='production_email',
        ),
        migrations.RenameField(
            model_name='aboutmodel',
            old_name='pro_mobile',
            new_name='production_mobile',
        ),
        migrations.RemoveField(
            model_name='aboutmodel',
            name='op_address1',
        ),
        migrations.RemoveField(
            model_name='aboutmodel',
            name='op_address2',
        ),
        migrations.RemoveField(
            model_name='aboutmodel',
            name='op_city',
        ),
        migrations.RemoveField(
            model_name='aboutmodel',
            name='op_country',
        ),
        migrations.RemoveField(
            model_name='aboutmodel',
            name='pro_address1',
        ),
        migrations.RemoveField(
            model_name='aboutmodel',
            name='pro_address2',
        ),
        migrations.RemoveField(
            model_name='aboutmodel',
            name='pro_city',
        ),
        migrations.RemoveField(
            model_name='aboutmodel',
            name='pro_country',
        ),
        migrations.AddField(
            model_name='aboutmodel',
            name='operation_address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aboutmodel',
            name='production_address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gamegenre',
            name='game_genre',
            field=models.CharField(choices=[('STRATEGY', 'Strategy'), ('---', '---'), ('HACK N SLASH', 'Hack n slash'), ('SHOOTING', 'Shooting'), ('PUZZLE', 'Puzzle'), ('SPACE', 'Space'), ('ADVENTURE', 'Adventure'), ('3D', '3d'), ('ACTION', 'Action'), ('BEAT EM UP', 'Beat em up'), ('3RD PERSON', '3rd Person'), ('TRIVIA', 'Trivia'), ('PLATFORMER', 'Platformer'), ('MMO', 'Mmo'), ('RPG', 'Rpg'), ('SPORTS', 'Sports'), ('RACING', 'Racing'), ('MOBA', 'Moba'), ('SIMULATION', 'Simulation'), ('INFINITE RUNNER', 'Infinite Runner'), ('FPS', 'Fps'), ('ARCADE', 'Arcade'), ('2D', '2D')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='portfoliomodel',
            name='category_type',
            field=models.CharField(choices=[('UNREAL', 'Unreal'), ('UNITY', 'Unity'), ('CONCEPT', 'Concept'), ('EXPERIMENTAL', 'Experimental'), ('3D', '3d')], max_length=12),
        ),
    ]
