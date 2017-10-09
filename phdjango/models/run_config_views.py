from django.core import serializers

from .models import *
from .generic_responses import *
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.forms import ModelForm
from django.template.loader import render_to_string


class RunConfIndexView(generic.ListView):
    template_name = 'models/run-conf-index.html'
    context_object_name = 'latest_run_conf_list'

    def get_queryset(self):
        """Return the last five created models."""
        return ModelRunConfiguration.objects.order_by('-created_at')


def get_model_run_config_view(request, model_run_config_id):
    run_config = get_object_or_404(ModelRunConfiguration, pk=model_run_config_id)
    data = serializers.serialize('json', [run_config], indent = 2, use_natural_foreign_keys=True)
    return render(request, 'models/run-config-detail.html', {
        "data": data,
        "object": run_config
    })


def create_model_run_config(request):
    model_run_config = ModelRunConfiguration()
    model_run_config.save()
    return HttpResponseRedirect(reverse('models:model-run-config-edit-basic', args=(model_run_config.id,)))


def create_learning(request, model_run_config_id, key):
    model_run_config = get_object_or_404(ModelRunConfiguration, pk=model_run_config_id)
    firm_config = getattr(model_run_config, key)
    learning = Learning()
    learning.firm_run_configuration = firm_config
    learning.save()
    return HttpResponseRedirect(
        reverse('models:model-run-config-edit-firm_config-edit_learning', args=(model_run_config_id, key, learning.id)))


def edit_learning(request, model_run_config_id, learning_id, key):
    class EntityForm(ModelForm):
        class Meta:
            model = Learning
            exclude = ['firm_run_configuration']
    learning = get_object_or_404(Learning, pk=learning_id)
    form = EntityForm(request.POST or None, instance=learning)
    if form.is_valid():
        my_model = form.save()
        my_model.save()
        return HttpResponseRedirect(reverse('models:model-run-config-edit-' + key, args=(model_run_config_id,)))

    return render(request, 'models/firm-learning.html', {
        'form': form,
        'model_run_config_id': model_run_config_id,
        'learning_id': learning_id,
        'key': key
    })


def delete_learning(request, model_run_config_id, learning_id, key):
    learning = get_object_or_404(Learning, pk=learning_id)
    learning.delete()
    return HttpResponseRedirect(reverse('models:model-run-config-edit-firm_config', args=(model_run_config_id, key)))


def edit_model_run_config_household(request, model_run_config_id):
    return generic_model_run_config_entry(request, model_run_config_id, cls=HouseholdRunConfiguration, key='household_config')


def edit_model_run_config_government(request, model_run_config_id):
    return generic_model_run_config_entry(request, model_run_config_id, cls=GovernmentRunConfiguration, key='government_config')


def edit_model_run_config_firm(request, model_run_config_id, key):
    model_run_config = get_object_or_404(ModelRunConfiguration, pk=model_run_config_id)
    firm_config = getattr(model_run_config, key)
    firm_learnings = []
    if firm_config is not None:
        firm_learnings = Learning.objects.filter(firm_run_configuration__in=[firm_config.id]).all()
    extra = render_to_string('models/firm-learnings.html', {
        'model_run_config_id': model_run_config_id,
        'firm_learnings': firm_learnings,
        'key': key
    })

    return generic_model_run_config_entry(
        request,
        model_run_config_id,
        cls=FirmRunConfiguration,
        extra=extra,
        key=key
    )


def edit_model_run_config_firm_raw(request, model_run_config_id):
    return edit_model_run_config_firm(request, model_run_config_id, 'raw_firm_config')


def edit_model_run_config_firm_capital(request, model_run_config_id):
    return edit_model_run_config_firm(request, model_run_config_id, 'capital_firm_config')


def edit_model_run_config_firm_production(request, model_run_config_id):
    return edit_model_run_config_firm(request, model_run_config_id, 'production_firm_config')


def edit_model_run_config_outside_world(request, model_run_config_id):
    return generic_model_run_config_entry(request, model_run_config_id, cls=OutsideWorldRunConfiguration, key='production_firm_config')


def edit_model_run_config(request, model_run_config_id):
    class EntityForm(ModelForm):
        class Meta:
            model = ModelRunConfiguration
            exclude = ['raw_firm_config', 'capital_firm_config', 'production_firm_config',
                       'household_config', 'government_config', 'outside_world_config']

    model_run_config = get_object_or_404(ModelRunConfiguration, pk=model_run_config_id)

    key = 'basic'
    form = EntityForm(request.POST or None, instance=model_run_config)
    if form.is_valid():
        my_model = form.save()
        my_model.save()
        return HttpResponseRedirect(reverse('models:model-config-edit-' + key, args=(model_run_config.id,)))

    return render(request, 'models/model-run-config-edit-generic-child.html', {
        'form': form,
        'model_run_config_id': model_run_config_id,
        'key': key
    })