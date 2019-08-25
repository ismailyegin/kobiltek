from django import forms
from django.forms import ModelForm

from wushu.models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person

        fields = (
            'tc', 'height', 'weight', 'birthDate')
        widgets = {

            'tc': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'T.C. Kimlik Numarası'}),

            'height': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Boy'}),

            'weight': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kilo'}),

            'birthDate': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker', 'autocomplete': 'off',
                       'onkeydown': 'return false','placeholder': 'Doğum Tarihi'}),

        }
