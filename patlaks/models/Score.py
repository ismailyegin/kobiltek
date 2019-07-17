from django.db import models


class Score(models.Model):
    competitor = models.ForeignKey('Competitor',on_delete=models.CASCADE, null=True, blank=True)
    score = models.BigIntegerField( null=True, blank=True)
    creationDate = models.DateTimeField(auto_now_add=True, verbose_name='Kayıt Tarihi')

