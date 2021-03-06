from django import forms
from django.forms import ModelForm

from wushu.models.CategoryItem import  CategoryItem
from wushu.models.Level import Level
from wushu.models.EnumFields import EnumFields


class GradeForm(ModelForm):
    definition = forms.ModelChoiceField(queryset=CategoryItem.objects.filter(forWhichClazz='COACH_GRADE'),
                                        to_field_name='name',
                                        empty_label="Seçiniz",
                                        label="Kademe",
                                        widget=forms.Select(
                                            attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                   'style': 'width: 100%; '}))

    class Meta:
        model =Level

        fields = (
            'startDate', 'definition', 'dekont', 'branch')

        labels = {'startDate': 'Hak Kazanma Tarihi', 'branch': 'Branş'}

        widgets = {

            'startDate': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker4', 'autocomplete': 'off',
                       'onkeydown': 'return false'}),
            'branch': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                          'style': 'width: 100%; '}),

        }
