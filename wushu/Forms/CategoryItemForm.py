from django import forms
from django.forms import ModelForm

from wushu.models import CategoryItem


class CategoryItemForm(ModelForm):
    parent = forms.ModelChoiceField(queryset=CategoryItem.objects.filter(forWhichClazz='BELT'),
                                    to_field_name='name',
                                    required=False,
                                    empty_label="Seçiniz",
                                    label="Üst Kuşak",
                                    widget=forms.Select(
                                        attrs={'class': 'form-control select2 select2-hidden-accessible',
                                               'style': 'width: 100%; '}))

    class Meta:
        model = CategoryItem
        fields = ('name', 'parent', 'branch', 'isFirst')
        labels = {'name': 'Tanımı', 'branch': 'Branş', 'isFirst': 'İlk Kuşak mı ?'}
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control ', 'required': 'required'}),
            'branch': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                          'style': 'width: 100%; '}),
            'isFirst': forms.CheckboxInput()

        }
