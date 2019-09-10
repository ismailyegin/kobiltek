from wushu.models import Menu, MenuAdmin, MenuAthlete, MenuReferee, MenuCoach, MenuDirectory, MenuClubUser


def getMenu(request):
    menus = Menu.objects.all()
    return {'menus': menus}


def getAdminMenu(request):
    adminmenus = MenuAdmin.objects.all()
    return {'adminmenus': adminmenus}


def getAthleteMenu(request):
    athletemenus = MenuAthlete.objects.all()
    return {'athletemenus': athletemenus}


def getRefereeMenu(request):
    refereemenus = MenuReferee.objects.all()
    return {'refereemenus': refereemenus}


def getCoachMenu(request):
    coachmenus = MenuCoach.objects.all()
    return {'coachmenus': coachmenus}


def getDirectoryMenu(request):
    directorymenus = MenuDirectory.objects.all()
    return {'directorymenus': directorymenus}


def getClubUserMenu(request):
    clubusermenus = MenuClubUser.objects.all()
    return {'clubusermenus': clubusermenus}
