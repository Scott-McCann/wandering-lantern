# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-14 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tavern', '0002_auto_20160614_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='weapon_type_prof',
            field=models.CharField(choices=[('Simple', 'Simple'), ('Martial', 'Martial')], max_length=256),
        ),
    ]