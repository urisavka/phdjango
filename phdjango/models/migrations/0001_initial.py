# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-27 18:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FirmRunConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.FloatField(default=1000, verbose_name='Наявні гроші')),
                ('salary', models.FloatField(blank=True, null=True, verbose_name='Заробітна плата')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='Ціна')),
                ('plan', models.FloatField(blank=True, null=True, verbose_name='Плановий обсяг виробництва')),
                ('salary_budget', models.FloatField(blank=True, null=True, verbose_name='Бюджет на оплату праці')),
                ('labor_capacity', models.FloatField(blank=True, null=True, verbose_name='Планова кількість працівників')),
                ('demand_elasticity', models.FloatField(default=-5, verbose_name='Еластичність попиту на продукцію')),
                ('labor_productivity', models.FloatField(default=50, verbose_name='Продуктивність праці')),
                ('raw_productivity', models.FloatField(blank=True, null=True, verbose_name='Продуктивність сировини')),
                ('raw_need', models.FloatField(blank=True, null=True, verbose_name='Потреба в сировині')),
                ('raw_budget', models.FloatField(blank=True, null=True, verbose_name='Бюджет на закупівлю сировини')),
                ('capital_productivity', models.FloatField(blank=True, null=True, verbose_name='Продуктивність капіталу')),
                ('capital_need', models.FloatField(blank=True, null=True, verbose_name='Потреба в капіталі')),
                ('capital_budget', models.FloatField(blank=True, null=True, verbose_name='Бюджет на закупівлю капіталу')),
                ('capital_amortization', models.FloatField(blank=True, null=True, verbose_name='Амортизація капіталу')),
            ],
        ),
        migrations.CreateModel(
            name='FirmStructure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('raw_firm', 'Виробник сировини'), ('capital_firm', 'Виробник капіталу'), ('production_firm', 'Виробник споживчої продукції')], default='production_firm', max_length=1024, verbose_name='Тип фірми')),
                ('salary', models.BooleanField(default=False, verbose_name='Заробітна платна')),
                ('price', models.BooleanField(default=False, verbose_name='Ціна')),
                ('labor_capacity', models.BooleanField(default=False, verbose_name='Планова кількість працівників')),
                ('plan', models.BooleanField(default=False, verbose_name='Плановий обсяг виробництва')),
                ('salary_budget', models.BooleanField(default=False, verbose_name='Бюджет на оплату праці')),
                ('raw_need', models.NullBooleanField(default=False, verbose_name='Потреба в сировині')),
                ('raw_budget', models.NullBooleanField(default=False, verbose_name='Бюджет на закупівлю сировини')),
                ('capital_need', models.NullBooleanField(default=False, verbose_name='Потреба в капіталі')),
                ('capital_budget', models.NullBooleanField(default=False, verbose_name='Бюджет на закупівлю капіталу')),
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
                ('minimal_help', models.FloatField(null=True, verbose_name='Мінімальна допомога по безробіттю')),
            ],
        ),
        migrations.CreateModel(
            name='GovernmentStructure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income_tax', models.BooleanField(default=False, verbose_name='Податок на доходи фізичних осіб')),
                ('profit_tax', models.BooleanField(default=False, verbose_name='Податок на прибуток')),
                ('import_tax', models.BooleanField(default=False, verbose_name='Ввізне мито')),
                ('coefficient_help', models.BooleanField(default=False, verbose_name='Коефіцієнт розрахунку допомоги по безробіттю')),
                ('minimal_help', models.BooleanField(default=False, verbose_name='Мінімальна допомога по безробіттю')),
            ],
        ),
        migrations.CreateModel(
            name='HouseholdRunConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(null=True, verbose_name='Кількість домогосподарств')),
                ('consumption_need', models.FloatField(null=True, verbose_name='Потреба в споживчій продукції')),
                ('consumption_budget', models.DecimalField(decimal_places=2, max_digits=20, null=True, verbose_name='Бюджет на споживання')),
            ],
        ),
        migrations.CreateModel(
            name='HouseholdStructure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumption_need', models.BooleanField(default=False, verbose_name='Потреба в споживчій продукції')),
                ('consumption_budget', models.BooleanField(default=False, verbose_name='Бюджет на споживання')),
            ],
        ),
        migrations.CreateModel(
            name='Learning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(choices=[('intuitive', 'Інтуїтивний метод'), ('extrapolation', 'Метод екстраполяції тенденції'), ('moses', 'Метод маржі прибутку'), ('random', 'Випадковий вибір'), ('rational', 'Раціональний вибір'), ('nonconscious', 'Несвідоме навчання'), ('qlearning', 'Q-навчання'), ('hierarchical', 'Ієрархічна база правил'), ('lcs', 'Система лінійних класифікаторів'), ('regression_decision_tree', 'Регресійне дерево рішень'), ('perceptron', 'Одношаровий персептрон'), ('svm', 'Система опорних векторів'), ('classification_decision_tree', 'Класифікаційне дерево рішень')], default='random', max_length=1024, verbose_name='Метод навчання')),
                ('count', models.IntegerField(default=0, verbose_name='Кількість фірм такого типу')),
                ('firm_run_configuration', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='FirmRunConfiguration', to='models.FirmRunConfiguration')),
            ],
        ),
        migrations.CreateModel(
            name='ModelConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('title', models.CharField(max_length=1024, null=True, verbose_name='Назва конфігурації моделі')),
                ('outside_world', models.BooleanField(default=False, verbose_name='Зовнішній світ')),
                ('capital_firm_structure', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='CapitalFirm', to='models.FirmStructure')),
                ('government_structure', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='models.GovernmentStructure')),
                ('household_structure', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='models.HouseholdStructure')),
                ('production_firm_structure', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ProductionFirm', to='models.FirmStructure')),
                ('raw_firm_structure', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='RawFirm', to='models.FirmStructure')),
            ],
        ),
        migrations.CreateModel(
            name='ModelResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modelConfig', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='models.ModelConfig')),
            ],
        ),
        migrations.CreateModel(
            name='ModelRunConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('iterations', models.IntegerField(null=True, verbose_name='Кількість ітерацій')),
                ('initial_money', models.DecimalField(decimal_places=2, max_digits=20, null=True, verbose_name='Початковий обсяг грошової маси')),
                ('household_birth', models.IntegerField(null=True, verbose_name='Приріст чисельності домогосподарств')),
                ('firm_birth', models.IntegerField(null=True, verbose_name='Рівень появи нових фірм')),
                ('money_growth', models.DecimalField(decimal_places=2, max_digits=20, null=True, verbose_name='Приріст грошової маси')),
                ('capital_firm_config', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='CapitalFirm', to='models.FirmRunConfiguration')),
                ('government_config', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Government', to='models.GovernmentRunConfiguration')),
                ('household_config', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Household', to='models.HouseholdRunConfiguration')),
            ],
        ),
        migrations.CreateModel(
            name='OutsideWorldRunConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raw_price', models.DecimalField(decimal_places=2, max_digits=20, null=True, verbose_name='Ціна сировини')),
                ('capital_price', models.DecimalField(decimal_places=2, max_digits=20, null=True, verbose_name='Ціна капіталу')),
                ('good_price', models.DecimalField(decimal_places=2, max_digits=20, null=True, verbose_name='Ціна споживчого товару')),
                ('exchange_rate', models.FloatField(null=True, verbose_name='Курси обміну валют')),
                ('sell_probability', models.FloatField(null=True, verbose_name='Ймовірність купівлі товару внутрішньої фірми')),
            ],
        ),
        migrations.AddField(
            model_name='modelrunconfiguration',
            name='outside_world_config',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='OutsideWorld', to='models.OutsideWorldRunConfiguration'),
        ),
        migrations.AddField(
            model_name='modelrunconfiguration',
            name='production_firm_config',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ProductionFirm', to='models.FirmRunConfiguration'),
        ),
        migrations.AddField(
            model_name='modelrunconfiguration',
            name='raw_firm_config',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='RawFirm', to='models.FirmRunConfiguration'),
        ),
        migrations.AddField(
            model_name='modelresult',
            name='modelRunConfiguration',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='models.ModelRunConfiguration'),
        ),
    ]
