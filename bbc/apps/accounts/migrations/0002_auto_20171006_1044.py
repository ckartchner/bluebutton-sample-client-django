# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 10:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='access_key_id',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='access_key_reset',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='access_key_secret',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='organization_name',
        ),
    ]