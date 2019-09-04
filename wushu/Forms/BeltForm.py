from django import forms
from django.forms import ModelForm

from wushu.models import Level, CategoryItem
from wushu.models.EnumFields import EnumFields


class BeltForm(ModelForm):
    definition = forms.ModelChoiceField(queryset=CategoryItem.objects.filter(forWhichClazz='BELT'),
                                        to_field_name='name',
                                        empty_label="Seçiniz",
                                        label="Tanımı",
                                        widget=forms.Select(
                                            attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                   'style': 'width: 100%; '}))

    class Meta:
        model = Level

        fields = (
            'startDate', 'durationDay', 'definition', 'branch', 'dekont')

        labels = {'startDate': 'Başlangıç Tarihi', 'durationDay': 'Süre', 'branch': 'Branş'}

        widgets = {

            'startDate': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker4', 'autocomplete': 'off',
                       'onkeydown': 'return false'}),

            'durationDay': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),

            'branch': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                          'style': 'width: 100%; '}),

        }
