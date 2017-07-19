from .models import *
from .generic_responses import *
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.forms import ModelForm
from django.core import serializers


class IndexView(generic.ListView):
    template_name = 'models/index.html'
    context_object_name = 'latest_model_list'

    def get_queryset(self):
        """Return the last five created models."""
        return ModelConfig.objects.order_by('-created_at')


class ModelConfigDetailView(generic.DetailView):
    model = ModelConfig
    template_name = 'models/config-detail.html'


class ModelResultDetailView(generic.DetailView):
    model = ModelResult
    template_name = 'models/result-detail.html'


def create_model_config(request):
    model_config = ModelConfig()
    model_config.save()
    return HttpResponseRedirect(reverse('models:model-config-edit-household_structure', args=(model_config.id,)))


def edit_model_config(request, model_config_id):
    return HttpResponseRedirect(reverse('models:model-config-edit-household_structure', args=(model_config_id,)))


def edit_model_config_household(request, model_config_id):
    return generic_model_config_entry(request, model_config_id, cls=HouseholdStructure, key='household_structure')


def edit_model_config_government(request, model_config_id):
    return generic_model_config_entry(request, model_config_id, cls=GovernmentStructure, key='government_structure')


def edit_model_config_production_firm(request, model_config_id):
    return generic_model_config_entry(request, model_config_id, cls=FirmStructure, key='production_firm_structure')


def edit_model_config_raw_firm(request, model_config_id):
    return generic_model_config_entry(request, model_config_id, cls=FirmStructure, key='raw_firm_structure')


def edit_model_config_capital_firm(request, model_config_id):
    return generic_model_config_entry(request, model_config_id, cls=FirmStructure, key='capital_firm_structure')


def edit_model_config_extra(request, model_config_id):
    class EntityForm(ModelForm):
        class Meta:
            model = ModelConfig
            fields = ['outside_world']

    model_config = get_object_or_404(ModelConfig, pk=model_config_id)

    key = 'extra'
    form = EntityForm(request.POST or None, instance=model_config)
    if form.is_valid():
        my_model = form.save()
        my_model.save()
        return HttpResponseRedirect(reverse('models:model-config-edit-' + key, args=(model_config.id,)))

    return render(request, 'models/run-config-edit-generic-child.html', {
        'form': form,
        'model_config_id': model_config_id,
        'key': key
    })

def get_model_view(request, model_config_id):
    model_config = get_object_or_404(ModelConfig, pk=model_config_id)
    data = serializers.serialize('json', [model_config], use_natural_foreign_keys=True, use_natural_primary_keys=True)
    return render(request, 'models/config-detail.html', {
        "data": data,
        "object": model_config
    })



def prepareRun(request):
    class ModelResultForm(ModelForm):
        class Meta:
            model = ModelResult
            exclude = []

    form = ModelResultForm()
    return render(request, 'models/run-conf.html', {
        'form': form,
    })


def run(request):
    modelConfig = get_object_or_404(ModelConfig, pk=request.POST['modelConfig'])
    modelRunConfiguration = get_object_or_404(ModelRunConfiguration, pk=request.POST['modelRunConfiguration'])
    modelResult = ModelResult()
    modelResult.modelConfig = modelConfig
    modelResult.modelRunConfiguration = modelRunConfiguration
    modelResult.save()
    return HttpResponseRedirect(reverse('models:model-result-detail', args=(modelResult.id,)))
