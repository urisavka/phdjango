# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 17:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0006_auto_20170722_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firmrunconfiguration',
            name='demand_elasticity',
            field=models.FloatField(null=True, verbose_name='Еластичність попиту на продукцію'),
        ),
        migrations.AlterField(
            model_name='firmrunconfiguration',
            name='labor_productivity',
            field=models.FloatField(null=True, verbose_name='Продуктивність праці'),
        ),
        migrations.AlterField(
            model_name='firmrunconfiguration',
            name='learning_method',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='LearningMethod', to='models.Learning'),
        ),
    ]