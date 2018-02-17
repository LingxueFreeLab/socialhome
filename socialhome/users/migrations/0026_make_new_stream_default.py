# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-03 12:01
from __future__ import unicode_literals

from django.db import migrations
from django.db.migrations import RunPython


def forward(apps, schema_editor):
    UserPreferenceModel = apps.get_model("dynamic_preferences_users", "UserPreferenceModel")
    UserPreferenceModel.objects.filter(name='use_new_stream').update(raw_value='True')


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_user_picture_ppoi'),
        ('dynamic_preferences_users', '0001_initial'),
    ]

    operations = [
        RunPython(forward, RunPython.noop)
    ]