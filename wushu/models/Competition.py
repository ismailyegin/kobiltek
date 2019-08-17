import enum

from django.db import models

from wushu.models import EnumFields


class Competition(models.Model):
    creationDate = models.DateTimeField(auto_now_add=True)
    modificationDate = models.DateTimeField()
    name = models.CharField(blank=False, null=False, max_length=1000)
    startDate = models.DateTimeField()
    finishDate = models.DateTimeField()
    location = models.CharField(blank=False, null=False, max_length=1000)
    branch = enum.EnumField(EnumFields.BRANCH)
    status = enum.EnumField(EnumFields.COMPSTATUS)
    type = enum.EnumField(EnumFields.COMPTYPE)
