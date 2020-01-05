from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'is_active')
        labels = {'first_name': 'Ad', 'last_name': 'Soyad', 'email': 'Email'}
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control ', 'value': '', 'required': 'required'}),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control ', 'required': 'required'}),
            'email': forms.TextInput(attrs={'class': 'form-control ', 'required': 'required'}),

            'is_active': forms.CheckboxInput(attrs={'class': 'iCheck-helper'}),

        }

    def clean_email(self):

        data = self.cleaned_data['email']
        print(self.instance)
        if  self.instance is None:
            if User.objects.filter(email=data).exists():
                raise forms.ValidationError("This email already used")
            return data
        else:
            return data
