from django.contrib.auth.models import User
from django.db import models


class Competitor(models.Model):
    MALE = 'Erkek'
    FEMALE = 'Kadın'

    GENDER_CHOICES = (
        (MALE, 'Erkek'),
        (FEMALE, 'Kadın'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reference = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    profileImage = models.ImageField(upload_to='profile/', null=True, blank=True, verbose_name='Profil Resmi')
    mobilePhone = models.CharField(max_length=120, verbose_name='Telefon Numarası' ,null=True, blank=True)
    gender = models.CharField(max_length=128, verbose_name='Cinsiyeti', choices=GENDER_CHOICES, default=MALE)
    birthDate = models.DateField(null=True, verbose_name='Doğum Tarihi')
    creationDate = models.DateTimeField(auto_now_add=True, verbose_name='Kayıt Tarihi')
    modificationDate = models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi')
    country = models.ForeignKey('Country', on_delete=models.CASCADE, null=True, blank=True)
    iban = models.CharField(max_length=200, verbose_name='IBAN Numarası', null=True, blank=True)
    imei = models.CharField(max_length=200, verbose_name='IMEI', null=True, blank=True)

