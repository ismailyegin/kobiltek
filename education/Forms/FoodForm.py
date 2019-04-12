from education.models import Food

from django import forms
from django.forms import ModelForm


class FoodForm(ModelForm):

    class Meta:
        model = Food
        fields = {'menu', 'food_date'}

        widgets = {

            'menu': forms.TextInput(attrs={'class': 'form-control tags', 'id':'tags', 'placeholder': 'Menü', 'required': 'required','rows':3}),
            'food_date': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker'}),
        }
