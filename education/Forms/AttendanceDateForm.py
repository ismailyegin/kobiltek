import datetime

from django import forms


class AttendanceDateForm(forms.Form):
    birthDate = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control  pull-right', 'id': 'datepicker', 'autocomplete': 'off', 'onkeydown':'return false'}))

    def clean_date(self):
        birthDate = self.cleaned_data['birthDate']
        if birthDate > datetime.date.today():
            raise forms.ValidationError("The date cannot be in the past!")
        return birthDate