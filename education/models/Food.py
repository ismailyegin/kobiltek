from django.db import models


class Food(models.Model):

    menu = models.TextField(max_length=18500, null=True, blank=True, verbose_name="Yemek Menüsü")
    food_date = models.DateField(verbose_name="Yemek Tarihi")
    creation_date = models.DateField(auto_now_add=True)