# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-12 15:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charchitra', '0010_video_youtube_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dur_name', models.CharField(max_length=40, null=True)),
                ('v_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('v_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charchitra.Video')),
            ],
        ),
    ]