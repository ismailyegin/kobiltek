import enum

from django.db import models

from wushu.models import EnumFields
from wushu.models.CategoryItem import CategoryItem


class Level(models.Model):
    creationDate = models.DateTimeField(auto_now_add=True)
    modificationDate = models.DateTimeField(auto_now=True)
    levelType = models.CharField(null=True,max_length=329, blank=True)
    branch = models.CharField(null=True,max_length=329, blank=True)
    isActive = models.BooleanField(default=True)
    startDate = models.DateTimeField()
    expireDate = models.DateTimeField()
    durationDay = models.IntegerField()
    definition = models.ForeignKey(CategoryItem, on_delete=models.CASCADE)
