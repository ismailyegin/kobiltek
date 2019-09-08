from django import forms
from django.forms import ModelForm

from wushu.models import CategoryItem


class CategoryItemForm(ModelForm):
    parent = forms.ModelChoiceField(queryset=CategoryItem.objects.filter(forWhichClazz='BELT'),
                                        to_field_name='name',
                                        empty_label="Seçiniz",
                                        label="Üst Kuşak",
                                        widget=forms.Select(
                                            attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                   'style': 'width: 100%; '}))
    class Meta:
        model = CategoryItem
        fields = ('name','parent')
        labels = {'name': 'Tanımı'}
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control ',  'required': 'required'})
        }
