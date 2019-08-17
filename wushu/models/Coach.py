from django.db import models

from wushu.models import Person, Punishment


class Coach(models.Model):
    creationDate = models.DateTimeField(auto_now_add=True)
    modificationDate = models.DateTimeField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE())
    punishment = models.ForeignKey(Punishment, on_delete=models.CASCADE())
