from django.db import models


# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=120, verbose_name='İsim')
    surname = models.CharField(max_length=120, verbose_name='Soyisim')
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

    class Meta:
        verbose_name = 'Hasta'
        verbose_name_plural = 'Hastalar'


class Threat(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='Hasta')
    threatName = models.CharField(max_length=120, verbose_name='Muayene Adı')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Muayene Ücreti')
    creationDate = models.DateTimeField(auto_now_add=True, verbose_name='Muayene Tarihi')

    class Meta:
        verbose_name ='Muayene'
        verbose_name_plural = 'Muayeneler'


class CashMovement(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='Hasta')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Ödenen Ücret')
    creationDate = models.DateTimeField(auto_now_add=True, verbose_name='Muayene Tarihi')

    class Meta:
        verbose_name ='Ödeme'
        verbose_name_plural = 'Ödemeler'


class PayList(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='Hasta')
    debt = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Ödenen Ücret')
    modificationDate = models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi')