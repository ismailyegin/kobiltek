from django.db import models

from wushu.models.Athlete import Athlete


class YearCategory(models.Model):
    categoryName = models.CharField(max_length=255, null=True, blank=True)
    creationDate = models.DateTimeField(auto_now_add=True)
    operationDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.categoryName)

    class Meta:
        default_permissions = ()
