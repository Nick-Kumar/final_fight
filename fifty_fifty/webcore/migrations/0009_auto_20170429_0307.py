# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-29 03:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webcore', '0008_auto_20170429_0306'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employee',
            new_name='UserProfile',
        ),
    ]