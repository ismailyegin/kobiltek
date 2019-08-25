from django import forms
from django.forms import ModelForm

from wushu.models import CategoryItem


class CategoryItemForm(ModelForm):
    class Meta:
        model = CategoryItem
        fields = ('name',)
        labels = {'name': 'Tanımı'}
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control ',  'required': 'required'})

        }
