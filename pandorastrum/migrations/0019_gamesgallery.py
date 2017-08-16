# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-15 21:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pandorastrum', '0018_auto_20170815_0116'),
    ]

    operations = [
        migrations.CreateModel(
            name='GamesGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_name', models.CharField(max_length=400)),
                ('img', models.ImageField(blank=True, null=True, upload_to='gallery')),
                ('img_caption', models.CharField(max_length=500)),
            ],
        ),
    ]
