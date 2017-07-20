# coding=utf-8
from django.db import models


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


class HouseholdStructure(models.Model):
    consumption_need = models.BooleanField("Потреба в споживчій продукції", default=False)
    consumption_budget = models.BooleanField("Бюджет на споживання", default=False)

    def natural_key(self):
        return {
            "consumption_need": self.consumption_need,
            "consumption_budget": self.consumption_budget
        }


class FirmStructure(models.Model):
    # type = models.CharField("Тип фірми", choices=(
    #     ('raw_firm', 'Виробник сировини'),
    #     ('capital_firm', 'Виробник капіталу'),
    #     ('production_firm', 'Виробник споживчої продукції')
    # ), default='production_firm', max_length = 1024)
    salary = models.BooleanField("Заробітна платна", default=False)
    price = models.BooleanField("Ціна", default=False)
    workers_count = models.BooleanField("Планова кількість працівників", default=False)
    plan = models.BooleanField("Плановий обсяг виробництва", default=False)
    salary_budget = models.BooleanField("Бюджет на оплату праці", default=False)

    raw_need = models.BooleanField("Потреба в сировині", default=False)
    raw_budget = models.BooleanField("Бюджет на закупівлю сировини", default=False)

    capital_need = models.BooleanField("Потреба в капіталі", default=False)
    capital_budget = models.BooleanField("Бюджет на закупівлю капіталу", default=False)
    # learning = models.ManyToManyField(Learning)

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
    title = models.CharField(null=True, max_length=1024)
    # step 1
    production_firm_structure = models.ForeignKey(FirmStructure, related_name="ProductionFirm", null=True)
    raw_firm_structure = models.ForeignKey(FirmStructure, related_name="RawFirm", null=True)
    capital_firm_structure = models.ForeignKey(FirmStructure, related_name="CapitalFirm", null=True)

    household_structure = models.ForeignKey(HouseholdStructure, null=True)

    government_structure = models.ForeignKey(GovernmentStructure, null=True)
    outside_world = models.BooleanField("Зовнішній світ", default=False)

    def natural_key(self):
        return (self.title, self.created_at, ) + self.production_firm_structure.natural_key() + \
               self.raw_firm_structure.natural_key() + self.capital_firm_structure.natural_key() + \
               self.household_structure.natural_key() + self.government_structure.natural_key()

    natural_key.dependencies = ['phdjango.FirmStructure', 'phdjango.HouseholdStructure', 'phdjango.GovernmentStructure']

    def __str__(self):
        return "Модель " + str(self.title) if self.title is not None else "" + "створена " + self.created_at.strftime("%Y-%m-%d %H:%M:%S")


class ModelRunConfiguration(models.Model):
    title = models.CharField(null=True, max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return "Конфігурація " + str(self.title) if self.title is not None else "" + " створена " + self.created_at.strftime("%Y-%m-%d %H:%M:%S")


class ModelResult(models.Model):
    modelRunConfiguration = models.ForeignKey(ModelRunConfiguration, null=True)
    modelConfig = models.ForeignKey(ModelConfig, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return "Запуск " + self.created_at.strftime("%Y-%m-%d %H:%M:%S")
