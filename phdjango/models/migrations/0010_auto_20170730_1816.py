# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0009_auto_20170730_1545'),
    ]

    operations = [
        migrations.RenameField(
            model_name='governmentrunconfiguration',
            old_name='minimal_tax',
            new_name='minimal_help',
        ),
        migrations.AlterField(
            model_name='modelrunconfiguration',
            name='money_growth',
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True, verbose_name='Приріст грошової маси'),
        ),
    ]