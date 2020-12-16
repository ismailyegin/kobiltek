from django.db import models


class TaoluCategory(models.Model):
    categoryName = models.CharField(max_length=255, null=True, blank=True)
    isDuilian = models.BooleanField(null=True, blank=True)
    creationDate = models.DateTimeField(auto_now_add=True)
    operationDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.categoryName)
    #
    # class Meta:
    #     default_permissions = ()
