# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 04:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pandorastrum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogContentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraph', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog')),
                ('image_full_width', models.BooleanField(default=False)),
                ('related_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pandorastrum.BlogModel')),
            ],
        ),
    ]