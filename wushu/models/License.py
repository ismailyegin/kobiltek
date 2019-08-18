import enum

from django.db import models

from wushu.models import EnumFields
from wushu.models.CategoryItem import CategoryItem
from wushu.models.SportsClub import SportsClub


class License(models.Model):
    creationDate = models.DateTimeField(auto_now_add=True)
    modificationDate = models.DateTimeField(auto_now=True)
    branch = models.CharField(null=True,max_length=329, blank=True)
    sportsClub = models.ForeignKey(SportsClub, on_delete=models.CASCADE)
    licenseNo = models.CharField(blank=False, null=False, max_length=255)
    expireDate = models.DateTimeField()
    cityHeadShip = models.ForeignKey(CategoryItem, on_delete=models.CASCADE)
