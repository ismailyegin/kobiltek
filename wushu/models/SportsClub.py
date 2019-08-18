from django.db import models

from wushu.models import Person, Communication, CategoryItem, Coach
from wushu.models.Coach import Coach
from wushu.models.CategoryItem import CategoryItem


class SportsClub(models.Model):
    creationDate = models.DateTimeField(auto_now_add=True)
    modificationDate = models.DateTimeField(auto_now=True)
    name = models.CharField(blank=False, null=False, max_length=120)
    shortName = models.CharField(blank=False, null=False, max_length=120)
    foundingDate = models.CharField(blank=True, null=True, max_length=120)
    logo = models.ImageField
    #president = models.ForeignKey(Person, on_delete=models.CASCADE)
    #communications = models.ForeignKey(Communication, on_delete=models.CASCADE)
    cityHeadShip = models.ForeignKey(CategoryItem, on_delete=models.CASCADE)
    coachs = models.ForeignKey(Coach, on_delete=models.CASCADE)
