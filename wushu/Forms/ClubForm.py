from django import forms
from django.forms import ModelForm

from wushu.models import SportsClub


class ClubForm(ModelForm):
    class Meta:
        model = SportsClub

        fields = (
            'name', 'shortName', 'foundingDate', 'logo', 'clubMail')
        widgets = {

            'name': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Kulüp Adı'}),

            'shortName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kulüp Kısa Adı'}),

            'clubMail': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kulüp Mail'}),

            'foundingDate': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker', 'autocomplete': 'off',
                       'onkeydown': 'return false', 'placeholder': 'Kulüp Kuruluş Tarihi'}),

        }
