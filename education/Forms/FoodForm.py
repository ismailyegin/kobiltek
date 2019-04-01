from education.models import Food

from django import forms
from django.forms import ModelForm


class FoodForm(ModelForm):

    class Meta:
        model = Food
        fields = {'menu', 'foodDate'}

        widgets = {

            'menu': forms.Textarea(attrs={'class': 'form-control ', 'placeholder': 'Menü', 'required': 'required'}),
            'foodDate': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker'}),
        }
