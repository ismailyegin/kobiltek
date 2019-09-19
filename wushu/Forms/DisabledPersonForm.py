from django import forms
from django.forms import ModelForm

from wushu.models import Person


class DisabledPersonForm(ModelForm):
    class Meta:
        model = Person

        fields = (
            'tc', 'profileImage', 'height', 'weight', 'birthDate', 'bloodType', 'gender', 'birthplace', 'motherName',
            'fatherName')
        labels = {'tc': 'T.C.', 'gender': 'Cinsiyet'}

        widgets = {

            'tc': forms.TextInput(attrs={'class': 'form-control ', 'required': 'required', 'readonly': 'readonly'}),

            'height': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),

            'weight': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),

            'birthplace': forms.TextInput(
                attrs={'class': 'form-control ', 'value': '', 'required': 'required', 'readonly': 'readonly'}),

            'motherName': forms.TextInput(
                attrs={'class': 'form-control ', 'value': '', 'required': 'required', 'readonly': 'readonly'}),

            'fatherName': forms.TextInput(
                attrs={'class': 'form-control ', 'value': '', 'required': 'required', 'readonly': 'readonly'}),

            'birthDate': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker', 'autocomplete': 'off',
                       'onkeydown': 'return false', 'required': 'required', 'readonly': 'readonly'}),

            'bloodType': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                             'style': 'width: 100%; ', 'disabled': 'disabled'}),

            'gender': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                          'style': 'width: 100%; ', 'disabled': 'disabled'}),

        }
