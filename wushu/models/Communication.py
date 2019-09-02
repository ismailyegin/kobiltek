from django.db import models

from wushu.models.City import City
from wushu.models.Country import Country


class Communication(models.Model):
    postalCode = models.CharField(max_length=120, null=True, blank=True)
    phoneNumber = models.CharField(max_length=120, null=True, blank=True)
    phoneNumber2 = models.CharField(max_length=120, null=True, blank=True)
    address = models.TextField(max_length=250, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
