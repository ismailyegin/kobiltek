from django import forms
from django.forms import ModelForm

from wushu.models import BeltExam, Coach


class BeltExamForm(ModelForm):


    class Meta:
        model = BeltExam

        fields = (
            'examDate', 'coach', 'paymentType', 'dekont', 'dekontDate', 'dekontDescription')

        labels = {'examDate': 'Sınav Tarihi', 'coach': 'Sınavı Yapan Antrenör', 'paymentType': 'Ücret Gönderim Şekli',
                  'dekont': 'Dekont', 'dekontDate': 'Dekont Tarihi', 'dekontDescription': 'Dekont Açıklaması'}

        widgets = {

            'examDate': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker4', 'autocomplete': 'off',
                       'onkeydown': 'return false', 'required': 'required'}),

            'dekontDescription': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),

            'coach': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                         'style': 'width: 100%; ', 'required': 'required'}),

            'paymentType': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                               'style': 'width: 100%; ', 'required': 'required'}),

            'dekontDate': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker3', 'autocomplete': 'off',
                       'onkeydown': 'return false', 'required': 'required'}),

            'dekont': forms.FileInput()

        }
