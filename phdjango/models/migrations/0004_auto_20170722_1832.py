# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 16:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0003_auto_20170718_2132'),
    ]

    operations = [
        migrations.CreateModel(
            name='FirmRunConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('demand_elasticity', models.FloatField(verbose_name='Еластичність попиту на продукцію')),
                ('labor_productivity', models.FloatField(verbose_name='Продуктивність праці')),
                ('capital_productivity', models.FloatField(null=True, verbose_name='Продуктивність капіталу')),
                ('capital_amortization', models.FloatField(null=True, verbose_name='Амортизація капіталу')),
                ('raw_productivity', models.FloatField(null=True, verbose_name='Продуктивність сировини')),
                ('learning_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LearningMethod', to='models.Learning')),
            ],
        ),
        migrations.CreateModel(
            name='GovernmentRunConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income_tax', models.FloatField(null=True, verbose_name='Податок на доходи фізичних осіб')),
                ('profit_tax', models.FloatField(null=True, verbose_name='Податок на прибуток')),
                ('import_tax', models.FloatField(null=True, verbose_name='Ввізне мито')),
                ('coefficient_help', models.FloatField(null=True, verbose_name='Коефіцієнт розрахунку допомоги по безробіттю')),
                ('minimal_tax', models.FloatField(null=True, verbose_name='Мінімальна допомога по безробіттю')),
            ],
        ),
        migrations.CreateModel(
            name='HouseholdRunConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='Кількість домогосподарств')),
                ('consumption_need', models.FloatField(null=True, verbose_name='Потреба в споживчій продукції')),
                ('consumption_budget', models.FloatField(null=True, verbose_name='Бюджет на споживання')),
            ],
        ),
        migrations.CreateModel(
            name='OutsideWorldRunConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raw_price', models.FloatField(null=True, verbose_name='Ціна сировини')),
                ('capital_price', models.FloatField(null=True, verbose_name='Ціна капіталу')),
                ('good_price', models.FloatField(null=True, verbose_name='Ціна споживчого товару')),
                ('exchange_rate', models.FloatField(null=True, verbose_name='Курси обміну валют')),
                ('sell_probability', models.FloatField(null=True, verbose_name='Ймовірність купівлі товару внутрішньої фірми')),
            ],
        ),
        migrations.AddField(
            model_name='firmstructure',
            name='type',
            field=models.CharField(choices=[('raw_firm', 'Виробник сировини'), ('capital_firm', 'Виробник капіталу'), ('production_firm', 'Виробник споживчої продукції')], default='production_firm', max_length=1024, verbose_name='Тип фірми'),
        ),
        migrations.AddField(
            model_name='modelrunconfiguration',
            name='firm_birth',
            field=models.IntegerField(null=True, verbose_name='Рівень появи нових фірм'),
        ),
        migrations.AddField(
            model_name='modelrunconfiguration',
            name='household_birth',
            field=models.IntegerField(null=True, verbose_name='Приріст чисельності домогосподарств'),
        ),
        migrations.AddField(
            model_name='modelrunconfiguration',
            name='initial_money',
            field=models.FloatField(null=True, verbose_name='Початковий обсяг грошової маси'),
        ),
        migrations.AddField(
            model_name='modelrunconfiguration',
            name='iterations',
            field=models.IntegerField(null=True, verbose_name='Кількість ітерацій'),
        ),
        migrations.AddField(
            model_name='modelrunconfiguration',
            name='money_growth',
            field=models.FloatField(null=True, verbose_name='Приріст грошової маси-'),
        ),
        migrations.AlterField(
            model_name='modelconfig',
            name='title',
            field=models.CharField(max_length=1024, null=True, verbose_name='Назва конфігурації моделі'),
        ),
        migrations.AddField(
            model_name='modelrunconfiguration',
            name='firm_config',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Firm', to='models.FirmRunConfiguration'),
        ),
        migrations.AddField(
            model_name='modelrunconfiguration',
            name='government_config',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Government', to='models.GovernmentRunConfiguration'),
        ),
        migrations.AddField(
            model_name='modelrunconfiguration',
            name='household_config',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Household', to='models.HouseholdRunConfiguration'),
        ),
        migrations.AddField(
            model_name='modelrunconfiguration',
            name='outside_world_config',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='OutsideWorld', to='models.OutsideWorldRunConfiguration'),
        ),
    ]