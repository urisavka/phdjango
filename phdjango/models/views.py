from .models import *
from .generic_responses import *
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.forms import ModelForm


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
