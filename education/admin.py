from django.contrib import admin

# Register your models here.
from education.models import Menu


class MenuAdmin(admin.ModelAdmin):
    list_display = ('id','name','parent_id','is_parent')


admin.site.register(Menu, MenuAdmin)