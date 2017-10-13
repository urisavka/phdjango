# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-13 12:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FirmResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firm_id', models.IntegerField()),
                ('firm_type', models.CharField(choices=[('CapitalFirm', 'CapitalFirm'), ('RawFirm', 'RawFirm'), ('ProductionFirm', 'ProductionFirm')], max_length=1024)),
                ('decision_maker_type', models.CharField(max_length=1024, verbose_name=(('intuitive', 'Інтуїтивний метод'), ('extrapolation', 'Метод екстраполяції тенденції'), ('moses', 'Метод маржі прибутку'), ('random', 'Випадковий вибір'), ('rational', 'Раціональний вибір'), ('nonconscious', 'Несвідоме навчання'), ('qlearning', 'Q-навчання'), ('hierarchical', 'Ієрархічна база правил'), ('lcs', 'Система лінійних класифікаторів'), ('regression_decision_tree', 'Регресійне дерево рішень'), ('perceptron', 'Одношаровий персептрон'), ('svm', 'Система опорних векторів'), ('classification_decision_tree', 'Класифікаційне дерево рішень')))),
                ('firm_step', models.IntegerField()),
                ('money', models.FloatField()),
                ('price', models.FloatField()),
                ('salary', models.FloatField()),
                ('sold', models.FloatField()),
                ('sales', models.FloatField()),
                ('stock', models.FloatField()),
                ('profit', models.FloatField()),
                ('plan', models.IntegerField()),
                ('labor_capacity', models.IntegerField()),
                ('salary_budget', models.FloatField()),
                ('raw', models.FloatField(null=True)),
                ('raw_budget', models.FloatField(null=True)),
                ('raw_need', models.FloatField(null=True)),
                ('capital', models.FloatField(null=True)),
                ('capital_budget', models.FloatField(null=True)),
                ('capital_need', models.FloatField(null=True)),
                ('capital_expenses', models.FloatField(null=True)),
                ('workers', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FirmRunConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.FloatField(default=1000, verbose_name='Наявні гроші')),
                ('salary', models.FloatField(blank=True, default=20, null=True, verbose_name='Заробітна плата')),
                ('price', models.FloatField(blank=True, default=5, null=True, verbose_name='Ціна')),
                ('plan', models.FloatField(blank=True, null=True, verbose_name='Плановий обсяг виробництва')),
                ('salary_budget', models.FloatField(blank=True, null=True, verbose_name='Бюджет на оплату праці')),
                ('labor_capacity', models.FloatField(blank=True, null=True, verbose_name='Планова кількість працівників')),
                ('demand_elasticity', models.FloatField(default=-5, verbose_name='Еластичність попиту на продукцію')),
                ('labor_productivity', models.FloatField(default=50, verbose_name='Продуктивність праці')),
                ('raw_productivity', models.FloatField(blank=True, null=True, verbose_name='Продуктивність сировини')),
                ('raw_need', models.FloatField(blank=True, null=True, verbose_name='Потреба в сировині')),
                ('raw_budget', models.FloatField(blank=True, null=True, verbose_name='Бюджет на закупівлю сировини')),
                ('raw', models.FloatField(blank=True, null=True, verbose_name='Початкові запаси сировини')),
                ('capital_productivity', models.FloatField(blank=True, null=True, verbose_name='Продуктивність капіталу')),
                ('capital_need', models.FloatField(blank=True, null=True, verbose_name='Потреба в капіталі')),
                ('capital_budget', models.FloatField(blank=True, null=True, verbose_name='Бюджет на закупівлю капіталу')),
                ('capital_expenses', models.FloatField(blank=True, null=True, verbose_name='Інвестиції в капітал')),
                ('capital', models.FloatField(blank=True, null=True, verbose_name='Початкові запаси капіталу')),
                ('capital_amortization', models.FloatField(blank=True, null=True, verbose_name='Амортизація капіталу')),
            ],
        ),
        migrations.CreateModel(
            name='FirmStructure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('raw_firm', 'Виробник сировини'), ('capital_firm', 'Виробник капіталу'), ('production_firm', 'Виробник споживчої продукції')], default='production_firm', max_length=1024, verbose_name='Тип фірми')),
                ('salary', models.BooleanField(default=True, verbose_name='Заробітна платна')),
                ('price', models.BooleanField(default=True, verbose_name='Ціна')),
                ('labor_capacity', models.BooleanField(default=False, verbose_name='Планова кількість працівників')),
                ('plan', models.BooleanField(default=False, verbose_name='Плановий обсяг виробництва')),
                ('salary_budget', models.BooleanField(default=False, verbose_name='Бюджет на оплату праці')),
                ('raw_need', models.NullBooleanField(default=None, verbose_name='Потреба в сировині')),
                ('raw_budget', models.NullBooleanField(default=None, verbose_name='Бюджет на закупівлю сировини')),
                ('capital_need', models.NullBooleanField(default=None, verbose_name='Потреба в капіталі')),
                ('capital_budget', models.NullBooleanField(default=None, verbose_name='Бюджет на закупівлю капіталу')),
            ],
        ),
        migrations.CreateModel(
            name='GoodMarketResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step', models.IntegerField()),
                ('seller_id', models.IntegerField()),
                ('buyer_id', models.IntegerField(null=True)),
                ('quantity', models.FloatField()),
                ('money', models.FloatField()),
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
                ('income_tax', models.NullBooleanField(default=None, verbose_name='Податок на доходи фізичних осіб')),
                ('profit_tax', models.NullBooleanField(default=None, verbose_name='Податок на прибуток')),
                ('import_tax', models.NullBooleanField(default=None, verbose_name='Ввізне мито')),
                ('coefficient_help', models.NullBooleanField(default=None, verbose_name='Коефіцієнт розрахунку допомоги по безробіттю')),
                ('minimal_help', models.NullBooleanField(default=None, verbose_name='Мінімальна допомога по безробіттю')),
            ],
        ),
        migrations.CreateModel(
            name='HouseholdRunConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=500, null=True, verbose_name='Кількість домогосподарств')),
                ('consumption_need', models.FloatField(null=True, verbose_name='Потреба в споживчій продукції')),
                ('consumption_budget', models.FloatField(null=True, verbose_name='Бюджет на споживання')),
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
            name='LaborMarketResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step', models.IntegerField()),
                ('worker_id', models.IntegerField()),
                ('employer_id', models.IntegerField()),
                ('action', models.CharField(choices=[('hire', 'hire'), ('fire', 'fire')], max_length=4)),
                ('salary', models.FloatField()),
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
                ('outside_world', models.NullBooleanField(default=None, verbose_name='Зовнішній світ')),
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
                ('firm_result', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='models.FirmResult')),
                ('good_market_result', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='models.GoodMarketResult')),
                ('labor_market_result', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='models.LaborMarketResult')),
                ('model_config', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='models.ModelConfig')),
            ],
        ),
        migrations.CreateModel(
            name='ModelRunConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('iterations', models.IntegerField(default=10, verbose_name='Кількість ітерацій')),
                ('initial_money', models.FloatField(default=100000, verbose_name='Початковий обсяг грошової маси')),
                ('household_birth', models.IntegerField(default=10, verbose_name='Приріст чисельності домогосподарств')),
                ('firm_birth', models.IntegerField(default=0, verbose_name='Рівень появи нових фірм')),
                ('money_growth', models.FloatField(default=2000, verbose_name='Приріст грошової маси')),
                ('capital_firm_config', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='CapitalFirm', to='models.FirmRunConfiguration')),
                ('government_config', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Government', to='models.GovernmentRunConfiguration')),
                ('household_config', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Household', to='models.HouseholdRunConfiguration')),
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
        migrations.CreateModel(
            name='WorldResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('step', models.IntegerField()),
                ('raw_firms', models.IntegerField(null=True)),
                ('capital_firms', models.IntegerField(null=True)),
                ('production_firms', models.IntegerField()),
                ('households', models.IntegerField()),
                ('price', models.FloatField()),
                ('raw_price', models.FloatField(null=True)),
                ('capital_price', models.FloatField(null=True)),
                ('production_price', models.FloatField()),
                ('salary', models.FloatField()),
                ('raw_salary', models.FloatField(null=True)),
                ('capital_salary', models.FloatField(null=True)),
                ('production_salary', models.FloatField()),
                ('sold', models.FloatField()),
                ('raw_sold', models.FloatField(null=True)),
                ('capital_sold', models.FloatField(null=True)),
                ('production_sold', models.FloatField()),
                ('stock', models.FloatField()),
                ('raw_stock', models.FloatField(null=True)),
                ('capital_stock', models.FloatField(null=True)),
                ('production_stock', models.FloatField()),
                ('sales', models.FloatField()),
                ('raw_sales', models.FloatField(null=True)),
                ('capital_sales', models.FloatField(null=True)),
                ('production_sales', models.FloatField()),
                ('money', models.FloatField()),
                ('raw_money', models.FloatField(null=True)),
                ('capital_money', models.FloatField(null=True)),
                ('production_money', models.FloatField()),
                ('employed', models.IntegerField()),
                ('raw_employed', models.IntegerField(null=True)),
                ('capital_employed', models.IntegerField(null=True)),
                ('production_employed', models.IntegerField()),
                ('salary_budget', models.FloatField()),
                ('raw_salary_budget', models.FloatField(null=True)),
                ('capital_salary_budget', models.FloatField(null=True)),
                ('production_salary_budget', models.FloatField()),
                ('unemployment_rate', models.FloatField()),
                ('raw', models.FloatField(null=True)),
                ('raw_need', models.FloatField(null=True)),
                ('raw_budget', models.FloatField(null=True)),
                ('capital', models.FloatField(null=True)),
                ('capital_need', models.FloatField(null=True)),
                ('capital_budget', models.FloatField(null=True)),
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
            name='model_run_config',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='models.ModelRunConfiguration'),
        ),
        migrations.AddField(
            model_name='modelresult',
            name='world_result',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='models.WorldResult'),
        ),
    ]
