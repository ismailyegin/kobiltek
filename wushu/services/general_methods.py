from django.contrib.auth import logout
from django.contrib.auth.models import Permission
from django.shortcuts import redirect

from wushu.models import Menu, MenuAdmin, MenuAthlete, MenuReferee, MenuCoach, MenuDirectory, MenuClubUser, \
    SportClubUser, Person, Athlete, Coach, Judge, DirectoryMember


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


def show_urls(urllist, depth=0):
    urls = []
    # show_urls(urls.urlpatterns)
    for entry in urllist:

        urls.append(entry)
        perm = Permission(name=entry.name, codename=entry.pattern.regex.pattern, content_type_id=7)
        perm.save()
        if hasattr(entry, 'url_patterns'):
            show_urls(entry.url_patterns, depth + 1)

    return urls


def show_urls_deneme(urllist, depth=0):
    urls = []
    # show_urls(urls.urlpatterns)
    for entry in urllist:

        urls.append(entry)

        if hasattr(entry, 'url_patterns'):
            show_urls(entry.url_patterns, depth + 1)

    return urls


def control_access(request):

    group = request.user.groups.all()[0]

    permissions = group.permissions.all()

    is_exist = False

    for perm in permissions:

        if request.resolver_match.url_name == perm.name:
            is_exist = True

    if not is_exist:
        logout(request)
        return redirect('accounts:login')



def getProfileImage(request):
    if (request.user.id):
        current_user = request.user

        if current_user.groups.filter(name='KulupUye').exists():
            athlete = SportClubUser.objects.get(user=current_user)
            person = Person.objects.get(id=athlete.person.id)

        elif current_user.groups.filter(name='Sporcu').exists():
            athlete = Athlete.objects.get(user=current_user)
            person = Person.objects.get(id=athlete.person.id)

        elif current_user.groups.filter(name='Antrenor').exists():
            athlete = Coach.objects.get(user=current_user)
            person = Person.objects.get(id=athlete.person.id)

        elif current_user.groups.filter(name='Hakem').exists():
            athlete = Judge.objects.get(user=current_user)
            person = Person.objects.get(id=athlete.person.id)

        elif current_user.groups.filter(name='Yonetim').exists():
            athlete = DirectoryMember.objects.get(user=current_user)
            person = Person.objects.get(id=athlete.person.id)

        elif current_user.groups.filter(name='Admin').exists():
            person = dict()
            person['profileImage']= "profile/logo.png"

        else:
            person = None

        return {'person': person}

    return {}