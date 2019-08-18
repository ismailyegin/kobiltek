from django.db import models

from wushu.models.Level import Level
from wushu.models.Punishment import Punishment


class Judge(models.Model):
    creationDate = models.DateTimeField(auto_now_add=True)
    modificationDate = models.DateTimeField(auto_now=True)
    # person = models.ForeignKey(Person, on_delete=models.CASCADE)
    visa = models.ForeignKey(Level, on_delete=models.CASCADE)
    punishment = models.ForeignKey(Punishment, on_delete=models.CASCADE)
