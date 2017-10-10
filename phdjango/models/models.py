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
    labor_capacity = models.BooleanField("Планова кількість працівників", default=False)
    plan = models.BooleanField("Плановий обсяг виробництва", default=False)
    salary_budget = models.BooleanField("Бюджет на оплату праці", default=False)

    raw_need = models.NullBooleanField("Потреба в сировині", default=False, null = True)
    raw_budget = models.NullBooleanField("Бюджет на закупівлю сировини", default=False, null = True)

    capital_need = models.NullBooleanField("Потреба в капіталі", default=False, null = True)
    capital_budget = models.NullBooleanField("Бюджет на закупівлю капіталу", default=False, null = True)

    def natural_key(self):
        return {
            "salary": self.salary,
            "price": self.price,
            "labor_capacity": self.labor_capacity,
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
    minimal_help = models.BooleanField("Мінімальна допомога по безробіттю", default=False)

    def natural_key(self):
        return {
            "income_tax": self.income_tax,
            "profit_tax": self.profit_tax,
            "import_tax": self.import_tax,
            "coefficient_help": self.coefficient_help,
            "minimal_help": self.minimal_help
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

class FirmRunConfiguration(models.Model):
    money = models.FloatField("Наявні гроші", default=1000)

    salary = models.FloatField("Заробітна плата", null=True, blank=True)
    price = models.FloatField("Ціна", null=True, blank=True)
    plan = models.FloatField("Плановий обсяг виробництва", null=True, blank=True)
    salary_budget = models.FloatField("Бюджет на оплату праці", null=True, blank=True)
    labor_capacity = models.FloatField("Планова кількість працівників", null=True, blank=True)

    demand_elasticity = models.FloatField("Еластичність попиту на продукцію", default=-5)
    labor_productivity = models.FloatField("Продуктивність праці", default=50)

    raw_productivity = models.FloatField("Продуктивність сировини", null=True, blank=True)
    raw_need = models.FloatField("Потреба в сировині", null=True, blank=True)
    raw_budget = models.FloatField("Бюджет на закупівлю сировини", null=True, blank=True)

    capital_productivity = models.FloatField("Продуктивність капіталу", null=True, blank=True)
    capital_need = models.FloatField("Потреба в капіталі", null=True, blank=True)
    capital_budget = models.FloatField("Бюджет на закупівлю капіталу", null=True, blank=True)
    capital_expenses = models.FloatField("Інвестиції в капітал", null=True, blank=True)

    capital_amortization = models.FloatField("Амортизація капіталу", null = True, blank = True)

    def natural_key(self):
        learnings = Learning.objects.filter(firm_run_configuration__in=[self.id]).all()

        # @todo: replace with cute one liner :)
        learning_keys = []
        for learning in learnings:
            learning_keys.append({
                "method": learning.method,
                "count": learning.count
            })

        return {
            "money": self.money,
            "salary": self.price,
            "plan": self.plan,
            "salary_budget": self.salary_budget,
            "labor_capacity": self.labor_capacity,
            "demand_elasticity": self.demand_elasticity,
            "labor_productivity": self.labor_productivity,
            "raw_productivity": self.raw_productivity,
            "raw_need": self.raw_need,
            "raw_budget": self.raw_budget,
            "capital_productivity": self.capital_productivity,
            "capital_need": self.capital_need,
            "capital_budget": self.capital_budget,
            "capital_expenses": self.capital_expenses,
            "capital_amortization": self.capital_amortization,
            "learnings": learning_keys,
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
            "income_tax": self.income_tax,
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

    raw_firm_config = models.ForeignKey(FirmRunConfiguration, related_name="RawFirm", null=True)
    capital_firm_config = models.ForeignKey(FirmRunConfiguration, related_name="CapitalFirm", null=True)
    production_firm_config = models.ForeignKey(FirmRunConfiguration, related_name="ProductionFirm", null=True)

    household_config = models.ForeignKey(HouseholdRunConfiguration, related_name="Household", null=True)
    government_config = models.ForeignKey(GovernmentRunConfiguration, related_name="Government", null=True)
    outside_world_config = models.ForeignKey(OutsideWorldRunConfiguration, related_name="OutsideWorld", null=True)

    def natural_key(self):
        return (self.title, self.created_at, self.iterations, self.initial_money, self.household_birth, self.firm_birth,
                self.money_growth,) + self.raw_firm_config.natural_key() + self.capital_firm_config.natural_key() + \
               self.production_firm_config.natural_key() + self.household_config.natural_key() + self.government_config.natural_key() + \
               self.outside_world_config.natural_key()

    natural_key.dependencies = ['phdjango.FirmRunConfiguration', 'phdjango.HouseholdRunConfiguration',
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
    count = models.IntegerField("Кількість фірм такого типу", default=0)

    firm_run_configuration = models.ForeignKey(FirmRunConfiguration, related_name="FirmRunConfiguration", null=True)

    def __str__(self):
        return self.method + ":" + str(self.count)

    def __str__(self):
        return self.method + ":" + str(self.count)

    def __str__(self):
        return self.method + ":" + str(self.count)


class WorldResult(models.Model):
    date = models.DateTimeField()
    step = models.IntegerField()

    raw_firms = models.IntegerField(null = True)
    capital_firms = models.IntegerField(null = True)
    production_firms = models.IntegerField()
    households = models.IntegerField()
    price = models.FloatField()
    raw_price = models.FloatField(null = True)
    capital_price = models.FloatField(null = True)
    production_price = models.FloatField()
    salary = models.FloatField()
    raw_salary = models.FloatField(null = True)
    capital_salary = models.FloatField(null = True)
    production_salary = models.FloatField()
    sold = models.FloatField()
    raw_sold = models.FloatField(null = True)
    capital_sold = models.FloatField(null = True)
    production_sold = models.FloatField()
    stock = models.FloatField()
    raw_stock = models.FloatField(null = True)
    capital_stock = models.FloatField(null = True)
    production_stock = models.FloatField()
    sales = models.FloatField()
    raw_sales = models.FloatField(null = True)
    capital_sales = models.FloatField(null = True)
    production_sales = models.FloatField()
    money = models.FloatField()
    raw_money = models.FloatField(null = True)
    capital_money = models.FloatField(null = True)
    production_money = models.FloatField()
    employed = models.IntegerField()
    raw_employed = models.IntegerField(null = True)
    capital_employed = models.IntegerField(null = True)
    production_employed = models.IntegerField()
    salary_budget = models.FloatField()
    raw_salary_budget = models.FloatField(null = True)
    capital_salary_budget = models.FloatField(null = True)
    production_salary_budget = models.FloatField()
    unemployment_rate = models.FloatField()
    raw = models.FloatField(null = True)
    raw_need = models.FloatField(null = True)
    raw_budget = models.FloatField(null = True)
    capital = models.FloatField(null = True)
    capital_need = models.FloatField(null = True)
    capital_budget = models.FloatField(null = True)


class FirmResult(models.Model):
    firm_id = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    firm_type = models.CharField(choices =
                                 {('RawFirm', 'RawFirm'),
                                 ('CapitalFirm', 'CapitalFirm'),
                                 ('ProductionFirm', 'ProductionFirm')}, max_length = 1024)
    decision_maker_type = models.CharField((
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
    ), max_length=1024)
    firm_step = models.IntegerField()
    money = models.FloatField()
    price = models.FloatField()
    salary = models.FloatField()
    sold = models.FloatField()
    sales = models.FloatField()
    stock = models.FloatField()
    profit = models.FloatField()
    plan = models.IntegerField()
    labor_capacity = models.IntegerField()
    salary_budget = models.FloatField()
    raw = models.FloatField(null = True)
    raw_budget = models.FloatField(null = True)
    raw_need = models.FloatField(null = True)
    capital = models.FloatField(null = True)
    capital_budget = models.FloatField(null = True)
    capital_need = models.FloatField(null = True)
    capital_expenses = models.FloatField(null = True)
    workers = models.IntegerField()


class LaborMarketResult(models.Model):
    step = models.IntegerField()
    worker_id = models.IntegerField()
    employer_id = models.IntegerField()
    action = models.CharField(choices = {('hire', 'hire'), ('fire', 'fire')}, max_length=4)
    salary = models.FloatField()

class GoodMarketResult(models.Model):
    step = models.IntegerField()
    seller_id = models.IntegerField()
    buyer_id = models.IntegerField(null = True)
    quantity = models.FloatField()
    money = models.FloatField()


class ModelResult(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    model_run_config = models.ForeignKey(ModelRunConfiguration, null=True)
    model_config = models.ForeignKey(ModelConfig, null=True)

    world_result = models.ForeignKey(WorldResult, null = True)
    firm_result = models.ForeignKey(FirmResult, null=True)
    labor_market_result = models.ForeignKey(LaborMarketResult, null=True)
    good_market_result = models.ForeignKey(GoodMarketResult, null=True)



    def __str__(self):
        return "Запуск " + self.created_at.strftime("%Y-%m-%d %H:%M:%S")
