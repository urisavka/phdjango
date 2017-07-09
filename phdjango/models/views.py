from django.shortcuts import render
from .models import ModelConfig, ModelResult
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic


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


def run(request, model_config_id):
    modelConfing = get_object_or_404(ModelConfig, pk=model_config_id)
    modelResult = ModelResult()
    modelResult.modelConfig = modelConfing
    modelResult.save()
    return HttpResponseRedirect(reverse('models:model-result-detail', args=(modelResult.id,)))
