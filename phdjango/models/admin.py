# coding=utf-8
from django.contrib import admin
from django.forms import forms
from betterforms.forms import BetterModelForm
from .models import *


class ModelConfigAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Структура моделі", {
            'fields': (
                'structure_firms_producers',
                'structure_households',
                'structure_firms_capital',
                'structure_firms_raw',
                'structure_government',
                'structure_outside_world'
            )
        }),
        ('Фірми-виробники споживчої продукції. Параметри керування', {
            'fields': (
                'firm_parameters_salary',
                'firm_parameters_price',
                'firm_parameters_workers_count',
                'firm_parameters_salary_budget'
            ),
        }),
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super(ModelConfigAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['structure_firms_producers'].disabled = True
        form.base_fields['structure_households'].disabled = True
        return form


admin.site.register(ModelConfig, ModelConfigAdmin)
admin.site.register(ModelRunConfiguration)
admin.site.register(ModelResult)
admin.site.register(FirmStructure)
admin.site.register(Learning)
