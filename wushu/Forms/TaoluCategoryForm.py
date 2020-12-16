from django import forms
from django.forms import ModelForm

from wushu.models.TaoluCategory import TaoluCategory


class TaoluCategoryForm(ModelForm):
    class Meta:
        model = TaoluCategory
        fields = ('categoryName', 'isDuilian')
        labels = {'categoryName': 'Tanımı', 'isDuilian': 'Duilian mı?'}
        widgets = {
            'categoryName': forms.TextInput(
                attrs={'class': 'form-control ', 'required': 'required'}),
            'isDuilian': forms.CheckboxInput(attrs={'class': 'iCheck-helper'}),
        }
