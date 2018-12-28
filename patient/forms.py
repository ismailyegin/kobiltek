from django import forms
from django.forms import ModelForm

from patient.models import Patient, Threat


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ('name', 'surname', 'mobilePhone', 'birthDate', 'patientNumber', 'email', 'address', 'isActive')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control ', 'placeholder': 'Hasta Adı','value':''}),
            'surname': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Hasta Soyadı'}),
            'mobilePhone': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Telefon Numarası'}),
            'birthDate': forms.DateInput(attrs={'class': 'form-control ', 'data-input-mask': 'alias: yyyy-mm-dd', 'data-mask': ''}),
            'patientNumber': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Hasta Numarası'}),
            'email': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Email'}),
            'address': forms.Textarea(attrs={'class': 'form-control ', 'placeholder': 'Adres'}),
            'isActive': forms.CheckboxInput(attrs={'class': 'iCheck-helper'})

        }


class ThreatForm(ModelForm):
    patient: forms.ModelChoiceField(queryset=Patient.objects.all(), to_field_name='name')

    class Meta:
        model=Threat
        fields = ('patient', 'threatName', 'price')
        widgets = {

            'patient': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                           'style': 'width: 100%;'}),
            'threatName': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Tedavi adı'}),
        }




