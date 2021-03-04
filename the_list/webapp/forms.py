from django import forms
from django.forms import widgets

from webapp.models import status_choices


class ListForms(forms.Form):
    status = forms.ChoiceField(required=False, choices=status_choices, label='status')
    description = forms.CharField(max_length=200, min_length=5, required=True, label='description')
    created_at = forms.DateField(label='date', required=False, widget=widgets.DateInput(format='%m/%d/%Y', attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}))
    about_list = forms.CharField(max_length=3000, required=False, label='about_list', widget=widgets.Textarea)



