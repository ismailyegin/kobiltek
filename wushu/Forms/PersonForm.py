from django import forms
from django.forms import ModelForm

from wushu.models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person

        fields = (
            'tc', 'height', 'weight', 'birthDate', 'bloodType', 'gender')
        labels = {'tc': 'T.C.', 'gender': 'Cinsiyet'}

        widgets = {

            'tc': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'T.C. Kimlik Numarası'}),

            'height': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Boy'}),

            'weight': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kilo'}),

            'birthDate': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker', 'autocomplete': 'off',
                       'onkeydown': 'return false', 'placeholder': 'Doğum Tarihi'}),

            'bloodType': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                             'style': 'width: 100%; '}),

            'gender': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                          'style': 'width: 100%; '}),

        }
