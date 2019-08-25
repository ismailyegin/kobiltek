from django import forms
from django.forms import ModelForm

from wushu.models import Athlete


class AthleteForm(ModelForm):
    class Meta:
        model = Athlete

        fields = (
            'branch', 'beltStartDate', 'beltFinishDate')

        widgets = {

            'branch': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                          'style': 'width: 100%;'}),

            'beltStartDate': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker2', 'autocomplete': 'off',
                       'onkeydown': 'return false', 'placeholder': 'Kuşak Başlama Tarihi'}),

            'beltFinishDate': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker3', 'autocomplete': 'off',
                       'onkeydown': 'return false', 'placeholder': 'Kuşak Başlama Tarihi'}),

        }
