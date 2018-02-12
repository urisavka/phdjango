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

    history = run_ace.run_ace_from_json(modelConfigJson, modelRunConfigurationJson, seed = 0, learning_data=None)

    modelResult = ModelResult()
    modelResult.model_config = modelConfig
    modelResult.model_run_config = modelRunConfiguration
    modelResult.save()

    history_list = []

    for i in range(modelRunConfiguration.iterations):
        entry = WorldResult()
        for field in entry.__dict__:
            if field not in ['_state', 'id', 'model_result_id', 'date']:
                if isinstance(getattr(history['world_history'], field), list):
                    setattr(entry, field, getattr(history['world_history'], field)[i])
                else:
                    setattr(entry, field, getattr(history['world_history'], field))
        entry.model_result = modelResult
        entry.save()
        history_list.append(entry)

#    result = WorldResult.objects.bulk_create(history_list)

    history_list = []

    for firm_history in history['firm_history']:
        for i in range(modelRunConfiguration.iterations):
            entry = FirmResult()
            for field in entry.__dict__:
                if field not in ['_state', 'id', 'model_result_id', 'date']:
                    if isinstance(getattr(firm_history, field), list):
                        setattr(entry, field, getattr(firm_history, field)[i])
                    else:
                        setattr(entry, field, getattr(firm_history, field))
            entry.model_result = modelResult
            entry.save()
            history_list.append(entry)

#    result = FirmResult.objects.bulk_create(history_list)

    history_list = []

    for i in range(len(history['good_market_history'].step)):
        entry = GoodMarketResult()
        for field in entry.__dict__:
            if field not in ['_state', 'id', 'model_result_id', 'date']:
                setattr(entry, field, getattr(history['good_market_history'], field)[i])
        entry.model_result = modelResult
        entry.save()
        history_list.append(entry)

#    result = GoodMarketResult.objects.bulk_create(history_list)

    history_list = []

    for firm_history in history['labor_market_history']:
        for i in range(len(firm_history.step)):
            entry = LaborMarketResult()
            for field in entry.__dict__:
                if field not in ['_state', 'id', 'model_result_id', 'date']:
                    setattr(entry, field, getattr(firm_history, field)[i])
            entry.model_result = modelResult
            entry.save()
            history_list.append(entry)

    if 'government_history' in history:
        history_list = []

        for i in range(len(history['government_history'].step)):
            entry = GovernmentResult()
            for field in entry.__dict__:
                if field not in ['_state', 'id', 'model_result_id', 'date']:
                    setattr(entry, field, getattr(history['government_history'], field)[i])
            entry.model_result = modelResult
            entry.save()
            history_list.append(entry)

    if 'outside_world_history' in history:
        history_list = []

        for i in range(len(history['outside_world_history'].step)):
            entry = OutsideWorldResult()
            for field in entry.__dict__:
                if field not in ['_state', 'id', 'model_result_id', 'date']:
                    setattr(entry, field, getattr(history['outside_world_history'], field)[i])
            entry.model_result = modelResult
            entry.save()
            history_list.append(entry)

    return HttpResponseRedirect(reverse('models:model-result-detail', args=(modelResult.id,)))