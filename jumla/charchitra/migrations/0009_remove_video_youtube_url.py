# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-12 15:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charchitra', '0008_auto_20190212_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='youtube_url',
        ),
    ]
