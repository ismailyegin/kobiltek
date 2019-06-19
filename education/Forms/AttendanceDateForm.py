from django import forms


class AttendanceDateForm(forms.Form):
    birthDate = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control  pull-right', 'id': 'datepicker', 'autocomplete': 'off', 'onkeydown':'return false'}))


