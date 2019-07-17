from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=120, verbose_name='Ülke Adı')
