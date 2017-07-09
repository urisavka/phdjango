from django.db import models


class ModelConfig(models.Model):
    # general fields
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    title = models.CharField(null=True, max_length=1024)
    # step 1
    structure_firms_producers = models.BooleanField("Фірми-виробники споживчої продукції", default=True)
    structure_households = models.BooleanField("Домогосподарства", default=True)

    structure_firms_capital = models.BooleanField("Фірми-виробники капіталу", default=False)
    structure_firms_raw = models.BooleanField("Фірми-виробники сировини", default=False)
    structure_government = models.BooleanField("Держава", default=False)
    structure_outside_world = models.BooleanField("Зовнішній світ", default=False)

    #step 2
    firm_parameters_salary = models.BooleanField("Заробітна платна", default=False)
    firm_parameters_price = models.BooleanField("Ціна", default=False)
    firm_parameters_workers_count = models.BooleanField("Планова кількість працівників", default=False)
    firm_parameters_salary_budget = models.BooleanField("Бюджет на оплату праці", default=False)
    # ...

    def __str__(self):
        return "Модель створена " + self.created_at.strftime("%Y-%m-%d %H:%M:%S")


class ModelRunConfiguration(models.Model):
    title = models.CharField(null=True, max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return "Конфігурація " + self.title + " створена " + self.created_at.strftime("%Y-%m-%d %H:%M:%S")


class ModelResult(models.Model):
    modelConfig = models.ForeignKey(ModelConfig, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return "Запуск " + self.created_at.strftime("%Y-%m-%d %H:%M:%S")
