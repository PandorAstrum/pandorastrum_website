# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 04:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pandorastrum', '0013_auto_20170813_0915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamesmodelpage',
            name='game_title',
        ),
        migrations.RemoveField(
            model_name='gamesmodelpage',
            name='games_gallery',
        ),
        migrations.DeleteModel(
            name='GamesStoreModel',
        ),
        migrations.DeleteModel(
            name='IndexModelPage',
        ),
        migrations.DeleteModel(
            name='StoreLinkModel',
        ),
        migrations.DeleteModel(
            name='testModel',
        ),
        migrations.RenameField(
            model_name='gamesmodel',
            old_name='android_compatability',
            new_name='android',
        ),
        migrations.RenameField(
            model_name='gamesmodel',
            old_name='console_compatability',
            new_name='console',
        ),
        migrations.RenameField(
            model_name='gamesmodel',
            old_name='pc_compatability',
            new_name='multiplayer',
        ),
        migrations.RenameField(
            model_name='gamesmodel',
            old_name='web_compatability',
            new_name='pc',
        ),
        migrations.RemoveField(
            model_name='gamesmodel',
            name='game_name',
        ),
        migrations.AddField(
            model_name='gamesmodel',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gamesmodel',
            name='game_desc',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='gamesmodel',
            name='game_thumbnail',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='games'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gamesmodel',
            name='game_title',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gamesmodel',
            name='released_on',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gamesmodel',
            name='single_player',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='gamesmodel',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='gamesmodel',
            name='web',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='GamesGalleryModel',
        ),
        migrations.DeleteModel(
            name='GamesModelPage',
        ),
    ]
