# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-12 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charchitra', '0009_remove_video_youtube_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='youtube_url',
            field=models.URLField(max_length=300, null=True),
        ),
    ]