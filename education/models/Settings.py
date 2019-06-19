from django.db import models


class Settings(models.Model):
    name = models.CharField(blank=True, null=True, verbose_name="Ayar Adı",max_length=120)
    value = models.CharField(blank=True, null=True, verbose_name="Ayar Değeri",max_length=120)
    title = models.CharField(blank=True, null=True, verbose_name="Ayar Başlığı", max_length=120)

