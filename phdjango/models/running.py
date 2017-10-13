from .models import *
from .generic_responses import *
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from ace import run_ace

def run(request):
    modelConfig = get_object_or_404(ModelConfig, pk=request.POST['model_config'])
    modelRunConfiguration = get_object_or_404(ModelRunConfiguration, pk=request.POST['model_run_config'])
    modelConfigJson = serializers.serialize('json', [modelConfig], indent=2, use_natural_foreign_keys=True)
    modelRunConfigurationJson = serializers.serialize('json', [modelRunConfiguration], indent=2,
                                                      use_natural_foreign_keys=True)

    run_ace.run_ace(modelConfigJson, modelRunConfigurationJson)

    modelResult = ModelResult()
    modelResult.modelConfig = modelConfig
    modelResult.modelRunConfiguration = modelRunConfiguration
    modelResult.save()
    return HttpResponseRedirect(reverse('models:model-result-detail', args=(modelResult.id,)))