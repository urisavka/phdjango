# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-05 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='firmrunconfiguration',
            name='capital_expenses',
            field=models.FloatField(blank=True, null=True, verbose_name='Інвестиції в капітал'),
        ),
    ]
