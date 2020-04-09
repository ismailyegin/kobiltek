from urllib import request

from django import forms
from django.forms import ModelForm

from wushu.models import Communication
from wushu.models import SportsClub
from wushu.models import SportClubUser


class CommunicationSearchForm(ModelForm):
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(CommunicationSearchForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['city'].required = False
        # self.fields['country'].required=False
    class Meta:

        model = Communication

        fields = ('city',)
        labels = {
                  'city': 'İl'}
        widgets = {


            'city': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                        'style': 'width: 100%;'}),
            #
            # 'country': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
            #                                'style': 'width: 100%;'}),

        }

class ClubSearchForm(ModelForm):
    kisi = forms.ModelChoiceField(queryset=SportClubUser.objects.all(),
                                        to_field_name='user',
                                        empty_label="Seçiniz",
                                        label="Kulüp Yöneticisi",
                                        required=False,
                                        widget=forms.Select(
                                            attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                   'style': 'width: 100%; '}))

    class Meta:
        model = SportsClub

        fields = (
            'name', 'shortName','clubMail',)

        labels = {
            'name': 'Kulüp Adı',
            'shortName': 'Kulüp Kısa Adı',
            'clubMail': 'Kulüp Email',
            # 'isFormal' : 'Kulüp Türü'

        }
        widgets = {
            # 'isFormal': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
            #                                 'style': 'width: 100%; '}),

            'name': forms.TextInput(attrs={'class': 'form-control '}),

            'shortName': forms.TextInput(attrs={'class': 'form-control'}),

            'clubMail': forms.TextInput(attrs={'class': 'form-control'}),



        }


