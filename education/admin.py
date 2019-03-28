from django.contrib import admin

# Register your models here.
from education.models import Menu


class MenuAdmin(admin.ModelAdmin):

    class Meta:
        Menu

admin.site.register(Menu, MenuAdmin)