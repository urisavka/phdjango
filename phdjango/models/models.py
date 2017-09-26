# coding=utf-8
from django.db import models


class HouseholdStructure(models.Model):
    consumption_need = models.BooleanField("Потреба в споживчій продукції", default=False)
    consumption_budget = models.BooleanField("Бюджет на споживання", default=False)

    def natural_key(self):
        return {
            "consumption_need": self.consumption_need,
            "consumption_budget": self.consumption_budget
        }


class FirmStructure(models.Model):
    type = models.CharField("Тип фірми", choices=(
        ('raw_firm', 'Виробник сировини'),
        ('capital_firm', 'Виробник капіталу'),
        ('production_firm', 'Виробник споживчої продукції')
    ), default='production_firm', max_length = 1024)
    salary = models.BooleanField("Заробітна платна", default=False)
    price = models.BooleanField("Ціна", default=False)
    workers_count = models.BooleanField("Планова кількість працівників", default=False)
    plan = models.BooleanField("Плановий обсяг виробництва", default=False)
    salary_budget = models.BooleanField("Бюджет на оплату праці", default=False)

    raw_need = models.BooleanField("Потреба в сировині", default=False)
    raw_budget = models.BooleanField("Бюджет на закупівлю сировини", default=False)

    capital_need = models.BooleanField("Потреба в капіталі", default=False)
    capital_budget = models.BooleanField("Бюджет на закупівлю капіталу", default=False)

    def natural_key(self):
        return {
            "salary": self.salary,
            "price": self.price,
            "workers_count": self.workers_count,
            "plan": self.plan,
            "salary_budget": self.salary_budget,
            "raw_need": self.raw_need,
            "raw_budget": self.raw_budget,
            "capital_need": self.capital_need,
            "capital_budget": self.capital_budget
        }


class GovernmentStructure(models.Model):
    income_tax = models.BooleanField("Податок на доходи фізичних осіб", default=False)
    profit_tax = models.BooleanField("Податок на прибуток", default=False)
    import_tax = models.BooleanField("Ввізне мито", default=False)

    coefficient_help = models.BooleanField("Коефіцієнт розрахунку допомоги по безробіттю", default=False)
    minimal_tax = models.BooleanField("Мінімальна допомога по безробіттю", default=False)

    def natural_key(self):
        return {
            "income_tax": self.income_tax,
            "profit_tax": self.profit_tax,
            "import_tax": self.import_tax,
            "coefficient_help": self.coefficient_help,
            "minimal_tax": self.minimal_tax
        }


class ModelConfig(models.Model):
    # general fields
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    title = models.CharField("Назва конфігурації моделі", null=True, max_length=1024)
    # step 1
    production_firm_structure = models.ForeignKey(FirmStructure, related_name="ProductionFirm", null=True)
    raw_firm_structure = models.ForeignKey(FirmStructure, related_name="RawFirm", null=True)
    capital_firm_structure = models.ForeignKey(FirmStructure, related_name="CapitalFirm", null=True)

    household_structure = models.ForeignKey(HouseholdStructure, null=True)

    government_structure = models.ForeignKey(GovernmentStructure, null=True)
    outside_world = models.BooleanField("Зовнішній світ", default=False)

    def natural_key(self):
        return (self.title, self.created_at,) + self.production_firm_structure.natural_key() + \
               self.raw_firm_structure.natural_key() + self.capital_firm_structure.natural_key() + \
               self.household_structure.natural_key() + self.government_structure.natural_key()

    natural_key.dependencies = ['phdjango.FirmStructure', 'phdjango.HouseholdStructure', 'phdjango.GovernmentStructure']

    def __str__(self):
        return "Модель " + str(self.title) if self.title is not None else "" + "створена " + self.created_at.strftime(
            "%Y-%m-%d %H:%M:%S")


class RawFirmRunConfiguration(models.Model):
    demand_elasticity = models.FloatField("Еластичність попиту на продукцію", null=True, blank=True)

    labor_productivity = models.FloatField("Продуктивність праці", null=True, blank=True)

    def natural_key(self):
        return {
            "demand_elasticity": self.demand_elasticity,
            "labor_productivity": self.labor_productivity
        }

class CapitalFirmRunConfiguration(models.Model):
    demand_elasticity = models.FloatField("Еластичність попиту на продукцію", null=True, blank=True)

    labor_productivity = models.FloatField("Продуктивність праці", null=True, blank=True)

    raw_productivity = models.FloatField("Продуктивність сировини", null=True, blank=True)

    def natural_key(self):
        return {
            "demand_elasticity": self.demand_elasticity,
            "labor_productivity": self.labor_productivity,
            "raw_productivity": self.raw_productivity
        }

class ProductionFirmRunConfiguration(models.Model):
    demand_elasticity = models.FloatField("Еластичність попиту на продукцію", null=True, blank=True)

    labor_productivity = models.FloatField("Продуктивність праці", null=True, blank=True)

    capital_productivity = models.FloatField("Продуктивність капіталу", null=True, blank=True)
    capital_amortization = models.FloatField("Амортизація капіталу", null=True, blank=True)

    raw_productivity = models.FloatField("Продуктивність сировини", null=True, blank=True)

    def natural_key(self):
        return {
            "demand_elasticity": self.demand_elasticity,
            "labor_productivity": self.labor_productivity,
            "capital_productivity": self.capital_productivity,
            "capital_amortization": self.capital_amortization,
            "raw_productivity": self.raw_productivity
        }


class HouseholdRunConfiguration(models.Model):
    count = models.IntegerField("Кількість домогосподарств", null=True)

    consumption_need = models.FloatField("Потреба в споживчій продукції", null=True)
    consumption_budget = models.DecimalField("Бюджет на споживання", null=True, max_digits=20, decimal_places=2)

    def natural_key(self):
        return {
            "count": self.count,
            "consumption_need": self.consumption_need,
            "condumption_budget": self.consumption_budget
        }


class GovernmentRunConfiguration(models.Model):
    income_tax = models.FloatField("Податок на доходи фізичних осіб", null=True)
    profit_tax = models.FloatField("Податок на прибуток", null=True)
    import_tax = models.FloatField("Ввізне мито", null=True)

    coefficient_help = models.FloatField("Коефіцієнт розрахунку допомоги по безробіттю", null=True)
    minimal_help = models.FloatField("Мінімальна допомога по безробіттю", null=True)

    def natural_key(self):
        return {
            "raw_price": self.raw_price,
            "profit_tax": self.profit_tax,
            "import_tax": self.import_tax,
            "coefficient_help": self.coefficient_help,
            "minimal_help": self.minimal_help
        }


class OutsideWorldRunConfiguration(models.Model):
    raw_price = models.DecimalField("Ціна сировини", null=True, max_digits=20, decimal_places=2)
    capital_price = models.DecimalField("Ціна капіталу", null=True, max_digits=20, decimal_places=2)
    good_price = models.DecimalField("Ціна споживчого товару", null=True, max_digits=20, decimal_places=2)

    exchange_rate = models.FloatField("Курси обміну валют", null=True)
    sell_probability = models.FloatField("Ймовірність купівлі товару внутрішньої фірми", null=True)

    def natural_key(self):
        return {
            "raw_price": self.raw_price,
            "capital_price": self.capital_price,
            "good_price": self.good_price,
            "exchange_rate": self.exchange_rate,
            "sell_probability": self.sell_probability
        }



class ModelRunConfiguration(models.Model):
    title = models.CharField(null=True, max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    iterations = models.IntegerField("Кількість ітерацій", null=True)

    initial_money = models.DecimalField("Початковий обсяг грошової маси", null=True,max_digits=20,decimal_places=2)

    household_birth = models.IntegerField("Приріст чисельності домогосподарств", null=True)
    firm_birth = models.IntegerField("Рівень появи нових фірм", null=True)
    money_growth = models.DecimalField("Приріст грошової маси", null=True, max_digits=20, decimal_places=2)

    raw_firm_config = models.ForeignKey(RawFirmRunConfiguration, related_name="RawFirm", null=True)
    capital_firm_config = models.ForeignKey(CapitalFirmRunConfiguration, related_name="CapitalFirm", null=True)
    production_firm_config = models.ForeignKey(ProductionFirmRunConfiguration, related_name="ProductionFirm", null=True)
    household_config = models.ForeignKey(HouseholdRunConfiguration, related_name="Household", null=True)
    government_config = models.ForeignKey(GovernmentRunConfiguration, related_name="Government", null=True)
    outside_world_config = models.ForeignKey(OutsideWorldRunConfiguration, related_name="OutsideWorld", null=True)


    def natural_key(self):
        return (self.title, self.created_at,self.iterations, self.initial_money, self.household_birth, self.firm_birth,
                self.money_growth, ) + self.raw_firm_config.natural_key() + self.capital_firm_config.natural_key() + \
               self.production_firm_config.natural_key() + self.household_config.natural_key() + self.government_config.natural_key() + \
               self.outside_world_config.natural_key()

    natural_key.dependencies = ['phdjango.RawFirmRunConfiguration', 'phdjango.CapitalFirmRunConfiguration',
                                'phdjango.ProductionFirmRunConfiguration', 'phdjango.HouseholdRunConfiguration',
                                'phdjango.GovernmentRunConfiguration', 'phdjango.OutsideWorldRunConfiguration']


    def __str__(self):
        return "Сценарій " + str(
            self.title) if self.title is not None else "" + " створений " + self.created_at.strftime("%Y-%m-%d %H:%M:%S")


class Learning(models.Model):
    method = models.CharField("Метод навчання", choices=(
        ('intuitive', 'Інтуїтивний метод'),
        ('extrapolation', 'Метод екстраполяції тенденції'),
        ('moses', 'Метод маржі прибутку'),
        ('random', 'Випадковий вибір'),

        ('rational', 'Раціональний вибір'),
        ('nonconscious', 'Несвідоме навчання'),
        ('qlearning', 'Q-навчання'),

        ('hierarchical', 'Ієрархічна база правил'),
        ('lcs', 'Система лінійних класифікаторів'),
        ('regression_decision_tree', 'Регресійне дерево рішень'),

        ('perceptron', 'Одношаровий персептрон'),
        ('svm', 'Система опорних векторів'),
        ('classification_decision_tree', 'Класифікаційне дерево рішень'),
    ), default='random', max_length=1024)
    count = models.IntegerField("Кількість фірм такого типу")

#    firm_run_configuration = models.ForeignKey(FirmRunConfiguration, related_name="FirmRunConfiguration", null=True)


class ModelResult(models.Model):
    modelRunConfiguration = models.ForeignKey(ModelRunConfiguration, null=True)
    modelConfig = models.ForeignKey(ModelConfig, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return "Запуск " + self.created_at.strftime("%Y-%m-%d %H:%M:%S")
