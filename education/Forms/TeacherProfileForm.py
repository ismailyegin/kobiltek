from django import forms
from django.forms import ModelForm

from education.models import Teacher


class TeacherProfileForm(ModelForm):
    #profileImage = forms.ImageField(widget=forms.ClearableFileInput(
     #   attrs={'class': 'form-control-file'}))

    class Meta:
        model = Teacher
        fields = ('profileImage', 'address', 'mobilePhone', 'gender', 'tc', 'birthDate')
        widgets = {
            'address': forms.Textarea(attrs={'class': 'form-control ', 'placeholder': 'Adres','required': 'required'}),
            'mobilePhone': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Telefon Numarası'}),
            'gender': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                           'style': 'width: 100%;'}),
            'tc': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'T.C. Kimlik No'}),

            #'birthDate': forms.DateInput(
           #     attrs={'class': 'form-control ', 'data-input-mask': '"alias: yyyy-mm-dd', 'data-mask': '"'}),

            'birthDate': forms.DateInput(
                attrs={'class': 'form-control  pull-right' , 'id':'datepicker'}),


        }