import enum

from django.db import models

from wushu.models import EnumFields, CategoryItem


class Level(models.Model):
    creationDate = models.DateTimeField(auto_now_add=True)
    modificationDate = models.DateTimeField()
    levelType = enum.EnumField(EnumFields.LEVELTYPE)
    branch = enum.EnumField(EnumFields.BRANCH)
    isActive = models.BooleanField(default=True)
    startDate = models.DateTimeField()
    expireDate = models.DateTimeField()
    durationDay = models.IntegerField()
    definition = models.ForeignKey(CategoryItem, on_delete=models.CASCADE())
