from .models import ModelConfig, ModelRunConfiguration
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.forms import ModelForm
from django.http import HttpResponseRedirect


def generic_model_config_entry(request, model_config_id, cls, key, firmType=None):
    class EntityForm(ModelForm):
        class Meta:
            model = cls
            exclude = [] if firmType is None else ['type']

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


def generic_model_run_config_entry(request, model_run_config_id, cls, key):
    class EntityForm(ModelForm):
        class Meta:
            model = cls
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
        'key': key
    })