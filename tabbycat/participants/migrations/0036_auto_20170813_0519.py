# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-13 05:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0035_auto_20170813_0517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='efl',
        ),
        migrations.RemoveField(
            model_name='person',
            name='esl',
        ),
        migrations.RemoveField(
            model_name='person',
            name='novice',
        ),
    ]
