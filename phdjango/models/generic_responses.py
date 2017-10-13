from .models import ModelConfig, ModelRunConfiguration
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.contrib import messages


def generic_model_config_entry(request, model_config_id, cls, key, firmType=None):
    class EntityForm(ModelForm):
        class Meta:
            model = cls
            if key == 'raw_firm_structure':
                exclude = ['type', 'raw_need', 'raw_budget', 'capital_need', 'capital_budget']
            elif key == 'capital_firm_structure':
                exclude = ['type', 'capital_need', 'capital_budget']
            elif key == 'production_firm_structure':
                exclude = ['type']
            else:
                exclude = []


    model_config = get_object_or_404(ModelConfig, pk=model_config_id)
    entity = getattr(model_config, key)
    if entity is None:
        entity = cls()
        if firmType is not None:
            entity.type = firmType
        entity.save()
        setattr(model_config, key, entity)
        model_config.save()

    form = EntityForm(request.POST or None, instance=entity)
    if form.is_valid():
        my_model = form.save()
        my_model.save()
        return HttpResponseRedirect(reverse('models:model-config-edit-' + key, args=(model_config.id,)))

    return render(request, 'models/model-config-edit-generic-child.html', {
        'form': form,
        'model_config_id': model_config_id,
        'key': key
    })


def generic_model_run_config_entry(request, model_run_config_id, cls, key, extra=None):
    class EntityForm(ModelForm):
        class Meta:
            model = cls
            if key == 'raw_firm_config':
                exclude = ['raw_productivity', 'raw_need', 'raw_budget', 'capital_productivity', 'raw',
                           'capital_need', 'capital_budget', 'capital_expenses', 'capital_amortization',
                           'capital']
            elif key == 'capital_firm_config':
                exclude = ['capital', 'capital_productivity',
                           'capital_need', 'capital_budget', 'capital_expenses', 'capital_amortization']
            else:
                exclude = []

    model_run_config = get_object_or_404(ModelRunConfiguration, pk=model_run_config_id)
    entity = getattr(model_run_config, key)
    if entity is None:
        entity = cls()
        entity.save()
        setattr(model_run_config, key, entity)
        model_run_config.save()

    form = EntityForm(request.POST or None, instance=entity)
    if form.is_valid():
        my_model = form.save()
        my_model.save()
        return HttpResponseRedirect(reverse('models:model-run-config-edit-' + key, args=(model_run_config.id,)))

    return render(request, 'models/model-run-config-edit-generic-child.html', {
        'form': form,
        'model_run_config_id': model_run_config_id,
        'key': key,
        'extra': '' if extra is None else extra,
    })