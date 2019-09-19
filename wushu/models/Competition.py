import enum

from django.db import models

from wushu.models import EnumFields


class Competition(models.Model):
    creationDate = models.DateTimeField(auto_now_add=True)
    modificationDate = models.DateTimeField(auto_now=True)
    name = models.CharField(blank=False, null=False, max_length=1000)
    startDate = models.DateTimeField()
    finishDate = models.DateTimeField()
    location = models.CharField(blank=False, null=False, max_length=1000)
    branch = models.CharField(null=True,max_length=329, blank=True)
    status = models.CharField(null=True,max_length=329, blank=True)
    type = models.CharField(null=True,max_length=329, blank=True)

    class Meta:
        default_permissions = ()
