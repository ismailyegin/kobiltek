from django.contrib.auth.models import User
from django.db import models


class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profileImage = models.ImageField(upload_to='profile/parent/', null=True, blank=True)
    address = models.TextField(blank=True, null=True, verbose_name='Adres')
    mobilePhone = models.CharField(max_length=120, verbose_name='Telefon Numarası')


