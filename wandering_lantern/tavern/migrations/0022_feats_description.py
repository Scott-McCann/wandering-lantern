# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-16 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tavern', '0021_character_background'),
    ]

    operations = [
        migrations.AddField(
            model_name='feats',
            name='description',
            field=models.TextField(default='description'),
        ),
    ]