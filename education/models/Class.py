from django.db import models

from education.models import Student


class Class(models.Model):
    year1 = '2018-2019'
    year2 = '2019-2020'

    EDUCATION_YEAR = (
        (year1, '2018-2019'),
        (year2, '2019-2020'),
    )

    name = models.CharField(max_length=120, verbose_name='Sınıf Adı')
    education_year = models.CharField(max_length=128, verbose_name='Eğitim Yılı', choices=EDUCATION_YEAR, default=year1)
    creationDate = models.DateTimeField(auto_now_add=True, verbose_name='Kayıt Tarihi')
    modificationDate = models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi')
    students = models.ManyToManyField(Student, verbose_name='Öğrenci')






