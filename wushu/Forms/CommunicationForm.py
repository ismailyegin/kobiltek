from django import forms
from django.forms import ModelForm

from wushu.models import Communication


class CommunicationForm(ModelForm):
    class Meta:
        model = Communication

        fields = (
            'phoneNumber', 'address', 'postalCode', 'phoneNumber2', 'city', 'country')
        labels = {'phoneNumber': 'Cep Telefonu', 'phoneNumber2': 'Sabit Telefon', 'postalCode': 'Posta Kodu'}
        widgets = {

            'address': forms.Textarea(
                attrs={'class': 'form-control ', 'placeholder': 'Adres', 'rows': '2', 'required': 'required'}),

            'phoneNumber': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Cep Telefonu'}),


            'phoneNumber2': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Sabit Telefon'}),

            'postalCode': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Posta Kodu'}),

            'city': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                        'style': 'width: 100%; '}),

            'country': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                           'style': 'width: 100%; '}),

        }
