import enum

from django.db import models

from wushu.models.EnumFields import EnumFields
from wushu.models.CategoryItem import CategoryItem


class Level(models.Model):
    WAITED = 'Beklemede'
    APPROVED = 'Onaylandı'
    PROPOUND = 'Onaya Gönderildi'
    DENIED = 'Reddedildi'

    STATUS_CHOICES = (
        (APPROVED, 'Onaylandı'),
        (PROPOUND, 'Onaya Gönderildi'),
        (DENIED, 'Reddedildi'),
        (WAITED, 'Beklemede'),
    )

    levelType = models.CharField(max_length=128, verbose_name='Leveller', choices=EnumFields.LEVELTYPE.value)
    branch = models.CharField(max_length=128, verbose_name='Branş', choices=EnumFields.BRANCH.value)
    isActive = models.BooleanField(default=True)
    startDate = models.DateTimeField()
    expireDate = models.DateTimeField()
    durationDay = models.IntegerField()
    definition = models.ForeignKey(CategoryItem, on_delete=models.CASCADE)
    creationDate = models.DateTimeField(auto_now_add=True)
    modificationDate = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=128, verbose_name='Onay Durumu', choices=STATUS_CHOICES, default=WAITED)
