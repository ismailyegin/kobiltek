from django.contrib.auth.models import AbstractUser, User
from django.db import models


# Create your models here.
from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

from oxiterp import settings


class Patient(models.Model):
    name = models.CharField(max_length=120, verbose_name='Hasta Adı')
    surname = models.CharField(max_length=120, verbose_name='Hasta Soyadı')
    patientNumber = models.CharField(max_length=120, verbose_name='Hasta Kayıt Numarası')
    mobilePhone = models.CharField(max_length=120, verbose_name='Telefon Numarası')
    isActive = models.BooleanField(verbose_name='Aktif')
    email = models.CharField(max_length=120, verbose_name='Email')
    birthDate = models.DateField(null=True, verbose_name='Doğum Tarihi')

    address = models.TextField(blank=True, null=True, verbose_name='Adres')
    creationDate = models.DateTimeField(auto_now_add=True, verbose_name='Kayıt Tarihi')
    modificationDate = models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi')

    def __str__(self):
        return self.name + " " + self.surname

    def __unicode__(self):
        return self.name + " " + self.surname

    def get_absolute_url(self):
        return reverse('patient:hasta-duzenle', kwargs={'pk': self.pk})

    @property
    def _get_total_debt(self):
        totalthreat = Threat.objects.filter(patient=self).aggregate(Sum('price'))
        totalpayment = CashMovement.objects.filter(patient=self).aggregate(Sum('price'))

        if totalpayment['price__sum'] is None:
            totalpayment['price__sum'] = 0
        else:
            totalpayment['price__sum']=totalpayment['price__sum']
        if totalthreat['price__sum'] is None:
            return 0
        else:
            return totalthreat['price__sum']-totalpayment['price__sum']

    totalDebt = _get_total_debt

    class Meta:
        verbose_name = 'Hasta'
        verbose_name_plural = 'Hastalar'


class Threat(models.Model):
    patient = models.ForeignKey(Patient,  on_delete=models.CASCADE, verbose_name='Hasta')
    threatName = models.CharField(max_length=120, verbose_name='Muayene Adı')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Muayene Ücreti')
    creationDate = models.DateTimeField(auto_now_add=True, verbose_name='Muayene Tarihi')

    class Meta:
        verbose_name ='Muayene'
        verbose_name_plural = 'Muayeneler'


class CashMovement(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='Hasta')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Ödenen Ücret')
    creationDate = models.DateTimeField(auto_now_add=True, verbose_name='Ödeme Tarihi')

    class Meta:
        verbose_name ='Ödeme'
        verbose_name_plural = 'Ödemeler'


class PayList(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='Hasta')
    debt = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Ödenen Ücret')
    modificationDate = models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi')


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)

#yapılacak
#def create_profile(sender, **kwargs):
 #   user = kwargs["instance"]
  #  if kwargs["created"] and kwargs['user.group.name']:

   #     user_profile = UserProfile(user=user)
    #    user_profile.save()
#post_save.connect(create_profile, sender=User)