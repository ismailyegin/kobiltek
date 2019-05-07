from django.contrib.auth.models import User
from django.db import models

from education.models.Parent import Parent


class Student(models.Model):

    MALE = 'Erkek'
    FEMALE = 'Kadın'

    GENDER_CHOICES = (
        (MALE, 'Erkek'),
        (FEMALE, 'Kadın'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profileImage = models.ImageField(upload_to='profile/', null=True, blank=True, verbose_name='Profil Resmi')
    address = models.TextField(blank=True, null=True, verbose_name='Adres')
    mobilePhone = models.CharField(max_length=120, verbose_name='Telefon Numarası')
    studentNumber = models.CharField(max_length=128, verbose_name='Öğrenci Numarası')
    gender = models.CharField(max_length=128, verbose_name='Cinsiyeti', choices=GENDER_CHOICES, default=MALE)
    tc = models.CharField(max_length=128, null=True, blank=True, verbose_name='T.C. Kimlik Numarası')
    birthDate = models.DateField(null=True, verbose_name='Doğum Tarihi')
    creationDate = models.DateTimeField(auto_now_add=True, verbose_name='Kayıt Tarihi')
    modificationDate = models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi')
    parents = models.ManyToManyField(Parent)
    isAddedToClass = models.BooleanField(default=False)

    class Meta:
        permissions = (('student_add', 'Öğrenci Ekle'),('student_list', 'Öğrenci Liste'),('update_student', 'Öğrenci Güncelle'))


