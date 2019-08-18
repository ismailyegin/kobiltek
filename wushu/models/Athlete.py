from django.db import models


from wushu.models.Punishment import Punishment
from wushu.models.License import License
from wushu.models.SportsClub import SportsClub
from wushu.models.Level import Level



class Athlete(models.Model):
    creationDate = models.DateTimeField(auto_now_add=True)
    modificationDate = models.DateTimeField(auto_now=True)
    #person = models.ForeignKey(Person, on_delete=models.CASCADE)
    punishment = models.ForeignKey(Punishment, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    license = models.ForeignKey(License, on_delete=models.CASCADE)
