from django.db import models

from education.models import Student, Parent


class StudentParentRelation:
    student = models.ForeignKey(Student,on_delete=models.CASCADE, verbose_name='Öğrenci')
    parent = models.ForeignKey(Parent,on_delete=models.CASCADE,verbose_name="Veli")
    degree = models.CharField(max_length=120, verbose_name='Yakınlık')
    creationDate = models.DateTimeField(auto_now_add=True, verbose_name='Kayıt Tarihi')
    modificationDate = models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi')

