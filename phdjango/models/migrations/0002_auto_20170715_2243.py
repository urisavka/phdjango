# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 20:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modelconfig',
            old_name='capital_firm_structure_id',
            new_name='capital_firm_structure',
        ),
        migrations.RenameField(
            model_name='modelconfig',
            old_name='government_structure_id',
            new_name='government_structure',
        ),
        migrations.RenameField(
            model_name='modelconfig',
            old_name='household_structure_id',
            new_name='household_structure',
        ),
        migrations.RenameField(
            model_name='modelconfig',
            old_name='production_firm_structure_id',
            new_name='production_firm_structure',
        ),
        migrations.RenameField(
            model_name='modelconfig',
            old_name='raw_firm_structure_id',
            new_name='raw_firm_structure',
        ),
    ]