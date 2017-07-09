# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-09 19:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0003_modelconfig_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modelConfig', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.ModelConfig')),
            ],
        ),
    ]
