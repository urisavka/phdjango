# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 19:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_auto_20170715_2243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='firmstructure',
            name='learning',
        ),
        migrations.RemoveField(
            model_name='firmstructure',
            name='type',
        ),
    ]