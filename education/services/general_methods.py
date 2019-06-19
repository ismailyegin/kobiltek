from django.contrib.auth.models import Permission, User

from education.models import Menu


def getMenu(request):
    menus = Menu.objects.all()
    return {'menus': menus}


def deactiveUser(request,pk):
    user = User.objects.get(pk=pk)
    user.is_active = False
    user.save()
    return user


def activeUser(request,pk):
    user = User.objects.get(pk=pk)
    user.is_active = True
    user.save()
    return user















