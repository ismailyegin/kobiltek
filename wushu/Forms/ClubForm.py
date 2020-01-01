from django import forms
from django.forms import ModelForm

from wushu.models import SportsClub


class ClubForm(ModelForm):
    class Meta:
        model = SportsClub

        fields = (
            'name', 'shortName', 'foundingDate', 'logo', 'clubMail', 'isFormal')
        labels = {
            'name': 'Adı',
            'shortName': 'Kısa Adı',
            'foundingDate': 'Kuruluş Tarihi',
            'clubMail': 'Email',
            'isFormal' : 'Resmi mi?'

        }
        widgets = {

            'name': forms.TextInput(attrs={'class': 'form-control ', 'required': 'required'}),

            'shortName': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),

            'clubMail': forms.TextInput(attrs={'class': 'form-control'}),

            'foundingDate': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker', 'autocomplete': 'off',
                       'onkeydown': 'return false', 'required': 'required'}),

        }
