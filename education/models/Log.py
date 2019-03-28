from django.contrib.auth.models import User
from django.db import models


class Log(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=1280, null=True, )
    creationDate = models.DateTimeField(auto_now_add=True)
