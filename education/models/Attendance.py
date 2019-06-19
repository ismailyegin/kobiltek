from django.contrib.auth.models import User
from django.db import models

from education.models import Student, Class


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_object = models.ForeignKey(Class, on_delete=models.CASCADE, null=True)
    lecture_order = models.CharField(blank=True, null=True, max_length=120)
    date = models.DateField(auto_now_add=True)
    creationDate = models.DateTimeField(auto_now_add=True)
    taken_by_who = models.ForeignKey(User, on_delete=models.CASCADE)
    education_year = models.CharField(blank=True, null=True, max_length=120)
    education_season = models.CharField(blank=True, null=True, max_length=120)
    is_exist = models.BooleanField(default=False)
