from django.db import models

from wushu.models import City


class Communication(models.Model):
    phoneNumber = models.CharField(max_length=120, null=True, blank=True)
    address = models.TextField(blank=True, null=True, verbose_name='Adres')
