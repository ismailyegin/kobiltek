from django.db import models


class CategoryItem(models.Model):
    name = models.CharField(blank=False, null=False, max_length=255)
    forWhichClazz = models.CharField(blank=False, null=False, max_length=255)
    creationDate = models.DateTimeField(auto_now_add=True)
    modificationDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s ' % self.name
