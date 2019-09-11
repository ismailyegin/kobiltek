from django.db import models

from wushu.models import Coach, Athlete, CategoryItem, SportsClub


class BeltExam(models.Model):
    BANK = 'Banka'
    POSTA = 'Posta'
    PAYMENT_CHOICES = (
        (BANK, 'Banka'),
        (POSTA, 'Posta'),
    )
    WAITED = 'Beklemede'
    APPROVED = 'Onaylandı'
    PROPOUND = 'Onaya Gönderildi'
    DENIED = 'Reddedildi'

    STATUS_CHOICES = (
        (APPROVED, 'Onaylandı'),
        (PROPOUND, 'Onaya Gönderildi'),
        (DENIED, 'Reddedildi'),
        (WAITED, 'Beklemede'),
    )

    creationDate = models.DateTimeField(auto_now_add=True)
    modificationDate = models.DateTimeField(auto_now=True)
    examDate = models.DateField(null=False, blank=False)
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE, null=False, blank=False)
    paymentType = models.CharField(max_length=128, verbose_name='Ödeme Şekli', choices=PAYMENT_CHOICES, default=BANK)
    dekont = models.FileField(upload_to='dekont/', null=True, blank=True, verbose_name='Dekont ')
    dekontDate = models.DateField(null=False, blank=False)
    dekontDescription = models.CharField(max_length=255, null=False, blank=False)
    athletes = models.ManyToManyField(Athlete)
    status = models.CharField(max_length=128, verbose_name='Onay Durumu', choices=STATUS_CHOICES, default=WAITED)
    sportClub = models.ForeignKey(SportsClub, on_delete=models.CASCADE, null=False, blank=False)
