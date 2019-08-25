from django.db import models


class Person(models.Model):
    tc = models.CharField(max_length=120, null=True, blank=True)
    height = models.CharField(max_length=120, null=True, blank=True)
    weight = models.CharField(max_length=120, null=True, blank=True)
    birthDate = models.DateField(null=True, verbose_name='Doğum Tarihi')
