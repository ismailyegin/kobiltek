from django.forms import ModelForm

from wushu.models import DirectoryMember


class DirectoryForm(ModelForm):
    class Meta:
        model = DirectoryMember
