from django.db import models

from wushu.models.Athlete import Athlete
from wushu.models.TaoluCategori import TaoluCategori


class CompetitionCategori(models.Model):
    categori = models.ForeignKey(TaoluCategori, on_delete=models.CASCADE, verbose_name='Categori')
    athlete = models.ManyToManyField(Athlete)

    class Meta:
        default_permissions = ()
