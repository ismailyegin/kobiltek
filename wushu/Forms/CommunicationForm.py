from django import forms
from django.forms import ModelForm

from wushu.models import Communication


class CommunicationForm(ModelForm):
    class Meta:
        model = Communication

        fields = (
            'phoneNumber', 'address')
        widgets = {

            'address': forms.Textarea(
                attrs={'class': 'form-control ', 'placeholder': 'Adres', 'rows': '2', 'required': 'required'}),

            'phoneNumber': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Telefon Numarası'}),

        }
