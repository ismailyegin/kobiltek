from django import forms
from django.forms import ModelForm

from education.models import Class


class ClassForm(ModelForm):

    class Meta:
        model = Class
        fields = {'name', 'education_year'}

        widgets = {

            'name': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Sınıf Adı', 'required': 'required'}),
            'education_year': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                           'style': 'width: 100%;'}),
        }
