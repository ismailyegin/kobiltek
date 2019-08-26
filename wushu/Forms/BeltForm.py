from django import forms
from django.forms import ModelForm

from wushu.models import Level


class BeltForm(ModelForm):
    class Meta:
        model = Level

        fields = (
            'startDate', 'durationDay', 'definition')


        widgets = {

            'startDate': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker4', 'autocomplete': 'off',
                       'onkeydown': 'return false', 'placeholder': 'Başlangıç Tarihi'}),

            'durationDay': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Süresi(Gün)'}),

            'definition': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                              'style': 'width: 100%; '}),

        }
