import enum

from django.db import models

from wushu.models import EnumFields, SportsClub, CategoryItem


class License(models.Model):
    creationDate = models.DateTimeField(auto_now_add=True)
    modificationDate = models.DateTimeField()
    branch = enum.Enum(EnumFields)
    sportsClub = models.ForeignKey(SportsClub, on_delete=models.CASCADE())
    licenseNo = models.CharField(blank=False, null=False, max_length=255)
    expireDate = models.DateTimeField()
    cityHeadShip = models.ForeignKey(CategoryItem, on_delete=models.CASCADE())
