# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 02:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pandorastrum', '0011_auto_20170827_0340'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpcomingGamesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_name', models.CharField(blank=True, max_length=200, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('game_img', models.ImageField(blank=True, null=True, upload_to='upcoming')),
                ('milestone_first_init', models.DateField(blank=True, null=True)),
                ('milestone_second_alpha', models.DateField(blank=True, null=True)),
                ('milestone_third_beta', models.DateField(blank=True, null=True)),
                ('game_teaser_description', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='gamegenre',
            name='game_genre',
            field=models.CharField(choices=[('PUZZLE', 'Puzzle'), ('SIMULATION', 'Simulation'), ('TRIVIA', 'Trivia'), ('3RD PERSON', '3rd Person'), ('SPACE', 'Space'), ('2D', '2D'), ('RACING', 'Racing'), ('HACK N SLASH', 'Hack n slash'), ('MOBA', 'Moba'), ('INFINITE RUNNER', 'Infinite Runner'), ('BEAT EM UP', 'Beat em up'), ('FPS', 'Fps'), ('RPG', 'Rpg'), ('ADVENTURE', 'Adventure'), ('ARCADE', 'Arcade'), ('MMO', 'Mmo'), ('SHOOTING', 'Shooting'), ('ACTION', 'Action'), ('PLATFORMER', 'Platformer'), ('---', '---'), ('STRATEGY', 'Strategy'), ('SPORTS', 'Sports'), ('3D', '3d')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='portfoliomodel',
            name='category_type',
            field=models.CharField(choices=[('EXPERIMENTAL', 'Experimental'), ('UNITY', 'Unity'), ('CONCEPT', 'Concept'), ('3D', '3d'), ('UNREAL', 'Unreal')], max_length=12),
        ),
    ]
