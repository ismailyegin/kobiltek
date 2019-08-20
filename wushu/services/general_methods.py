from wushu.models import Menu, MenuAdmin


def getMenu(request):
    menus = Menu.objects.all()
    return {'menus': menus}


def getAdminMenu(request):
    adminmenus = MenuAdmin.objects.all()
    return {'adminmenus': adminmenus}
