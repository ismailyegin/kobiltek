from django import forms
from django.forms import ModelForm

from wushu.models import BeltExam, Coach, SportsClub


class BeltExamForm(ModelForm):
    sportClub = forms.ModelChoiceField(queryset=SportsClub.objects.all(),
                                        to_field_name='name',
                                        empty_label="Seçiniz",
                                        label="Kulüp",
                                        required=True,
                                        widget=forms.Select(
                                            attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                   'style': 'width: 100%; '}))

    coach = forms.ModelChoiceField(queryset=Coach.objects.all(),
                                   empty_label="Seçiniz",
                                   label="Sonavı Yapan Antrenör",
                                   required=True,
                                   widget=forms.Select(
                                       attrs={'class': 'form-control select2 select2-hidden-accessible',
                                              'style': 'width: 100%; '}))

    class Meta:
        model = BeltExam

        fields = (
            'examDate', 'coach', 'paymentType', 'dekont', 'dekontDate', 'dekontDescription','sportClub')

        labels = {'examDate': 'Sınav Tarihi', 'coach': 'Sınavı Yapan Antrenör', 'paymentType': 'Ücret Gönderim Şekli',
                  'dekont': 'Dekont', 'dekontDate': 'Dekont Tarihi', 'dekontDescription': 'Dekont Açıklaması', 'sportClub': 'Kulüp'}

        widgets = {

            'examDate': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker4', 'autocomplete': 'off',
                       'onkeydown': 'return false', 'required': 'required'}),

            'dekontDescription': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),

            'paymentType': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                               'style': 'width: 100%; ', 'required': 'required'}),

            'dekontDate': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker3', 'autocomplete': 'off',
                       'onkeydown': 'return false', 'required': 'required'}),

            'dekont': forms.FileInput()

        }
