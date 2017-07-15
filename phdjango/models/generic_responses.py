from .models import ModelConfig
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.forms import ModelForm
from django.http import HttpResponseRedirect


def generic_model_config_entry(request, model_config_id, cls, key):
    class EntityForm(ModelForm):
        class Meta:
            model = cls
            exclude = []

    model_config = get_object_or_404(ModelConfig, pk=model_config_id)
    entity = getattr(model_config, key)
    if entity is None:
        entity = cls()
        entity.save()
        setattr(model_config, key, entity)
        model_config.save()

    form = EntityForm(request.POST or None, instance=entity)
    if form.is_valid():
        my_model = form.save()
        my_model.save()
        return HttpResponseRedirect(reverse('models:model-config-edit-' + key, args=(model_config.id,)))

    return render(request, 'models/run-config-edit-generic-child.html', {
        'form': form,
        'model_config_id': model_config_id,
        'key': key
    })