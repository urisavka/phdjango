from .models import *
from django import forms
from .generic_responses import *
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.forms import ModelForm
from django.core import serializers
from django.contrib import messages

from django.shortcuts import render_to_response
from formtools.wizard.views import SessionWizardView

class TableForm(forms.Form):
    table = forms.ChoiceField(label='Вісь Х:',
                                choices={
                                    ("world_result", "Світ"),
                                    ("firm_result", "Фірми"),
                                    ("goodmarket_result", "Ринок товарів"),
                                    ("labor_market_result", "Ринок праці")})

class FieldForm(forms.Form):
    field = forms.ChoiceField(choices = ())


class TestWizard(SessionWizardView):
    form_list = [TableForm, FieldForm]
    def done(self, form_list, form_dict, **kwargs):
        return render(self.request, 'models/analyze', {
            'form_data': [form.cleaned_data for form in form_list],
        })


