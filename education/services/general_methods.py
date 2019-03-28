from django.contrib.auth.models import Permission

from education.models import Menu


def getMenu(request):
    menus = Menu.objects.all()
    return {'menus': menus}














