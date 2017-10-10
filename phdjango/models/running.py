from .models import *
from .generic_responses import *
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from ace import run

def run(request):
    modelConfig = get_object_or_404(ModelConfig, pk=request.POST['modelConfig'])
    modelRunConfiguration = get_object_or_404(ModelRunConfiguration, pk=request.POST['modelRunConfiguration'])
    modelConfigJson = serializers.serialize('json', [modelConfig], indent=2, use_natural_foreign_keys=True)
    modelRunConfigurationJson = serializers.serialize('json', [modelRunConfiguration], indent=2,
                                                      use_natural_foreign_keys=True)

    run(modelConfigJson, modelRunConfigurationJson)

    modelResult = ModelResult()
    modelResult.modelConfig = modelConfig
    modelResult.modelRunConfiguration = modelRunConfiguration
    modelResult.save()
    return HttpResponseRedirect(reverse('models:model-result-detail', args=(modelResult.id,)))