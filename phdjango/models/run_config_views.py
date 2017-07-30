from django.core import serializers

from .models import *
from .generic_responses import *
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.forms import ModelForm


class RunConfIndexView(generic.ListView):
    template_name = 'models/run-conf-index.html'
    context_object_name = 'latest_run_conf_list'

    def get_queryset(self):
        """Return the last five created models."""
        return ModelRunConfiguration.objects.order_by('-created_at')

def get_model_config_view(request, id):
    entity = get_object_or_404(ModelRunConfiguration, pk=id)
    data = serializers.serialize('json', [entity], indent = 2, use_natural_foreign_keys=True)
    return render(request, 'models/run-config-detail.html', {
        "data": data,
        "object": entity
    })

def create_model_run_config(request):
    model_run_config = ModelRunConfiguration()
    model_run_config.save()
    return HttpResponseRedirect(reverse('models:model-run-config-edit-basic', args=(model_run_config.id,)))


def edit_model_run_config_household(request, model_run_config_id):
    return generic_model_run_config_entry(request, model_run_config_id, cls=HouseholdRunConfiguration, key='household_config')


def edit_model_run_config_government(request, model_run_config_id):
    return generic_model_run_config_entry(request, model_run_config_id, cls=GovernmentRunConfiguration, key='government_config')


def edit_model_run_config_firm(request, model_run_config_id):
    return generic_model_run_config_entry(request, model_run_config_id, cls=FirmRunConfiguration, key='firm_config')


def edit_model_run_config_outside_world(request, model_run_config_id):
    return generic_model_run_config_entry(request, model_run_config_id, cls=OutsideWorldRunConfiguration, key='outside_world_config')


def edit_model_run_config(request, model_run_config_id):
    class EntityForm(ModelForm):
        class Meta:
            model = ModelRunConfiguration
            exclude = ['firm_config', 'household_config', 'government_config', 'outside_world_config']

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