from random import choices

from django.contrib.auth.models import User
from django.db import models

from wushu.models.Person import Person
from wushu.models.Communication import Communication
from wushu.models.EnumFields import EnumFields


class Athlete(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    communication = models.OneToOneField(Communication, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    branch = models.CharField(max_length=128, verbose_name='Branş', choices=EnumFields.BRANCH.value)
    beltStartDate = models.DateField(null=True, verbose_name='Kuşak Başlama Tarihi')
    beltFinishDate = models.DateField(null=True, verbose_name='Kuşak Bitiş Tarihi')

    creationDate = models.DateTimeField(auto_now_add=True)
    modificationDate = models.DateTimeField(auto_now=True)
