from django.contrib.auth.models import User
from django.db import models
from wushu.models.Communication import Communication
from wushu.models.Person import Person


class Coach(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    communication = models.OneToOneField(Communication, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    creationDate = models.DateTimeField(auto_now_add=True)
    modificationDate = models.DateTimeField(auto_now=True)
