from idlelib.idle_test.test_run import S
from itertools import product

from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.db.models import Q
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from wushu.Forms.BeltExamForm import BeltExamForm
from wushu.Forms.ClubForm import ClubForm
from wushu.Forms.ClubRoleForm import ClubRoleForm
from wushu.Forms.CommunicationForm import CommunicationForm
from wushu.Forms.DisabledCommunicationForm import DisabledCommunicationForm
from wushu.Forms.DisabledPersonForm import DisabledPersonForm
from wushu.Forms.DisabledSportClubUserForm import DisabledSportClubUserForm
from wushu.Forms.DisabledUserForm import DisabledUserForm
from wushu.Forms.PersonForm import PersonForm
from wushu.Forms.SportClubUserForm import SportClubUserForm
from wushu.Forms.UserForm import UserForm
from wushu.Forms.SearchClupForm import SearchClupForm
from wushu.Forms.PreRegidtrationForm import PreRegistrationForm
from wushu.Forms.UserSearchForm import UserSearchForm
from wushu.Forms.ClupUserSearchForm import ClubSearchForm

from wushu.models import SportsClub, SportClubUser, Communication, Person, BeltExam, Athlete, Coach, Level, CategoryItem
from wushu.models.ClubRole import ClubRole
from wushu.models.EnumFields import EnumFields
from wushu.models.PreRegistration import PreRegistration
from wushu.services import general_methods
from datetime import date,datetime
import datetime
from django.utils import timezone


from django.contrib.auth.models import Group, Permission, User

@login_required
def return_add_club(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    club_form = ClubForm()
    communication_form = CommunicationForm()

    if request.method == 'POST':

        club_form = ClubForm(request.POST, request.FILES)
        communication_form = CommunicationForm(request.POST, request.FILES)

        if club_form.is_valid():
            clubsave = SportsClub(name=club_form.cleaned_data['name'],
                                  shortName=club_form.cleaned_data['shortName'],
                                  foundingDate=club_form.cleaned_data['foundingDate'],
                                  logo=club_form.cleaned_data['logo'],
                                  clubMail=club_form.cleaned_data['clubMail'],
                                  isFormal=club_form.cleaned_data['isFormal'],

                                  )

            communication = communication_form.save(commit=False)
            communication.save()
            clubsave.communication = communication

            clubsave.save()

            mesaj = str(club_form.cleaned_data['name']) + ' Klubü ekledi   '
            log = general_methods.logwrite(request, request.user, mesaj)




            messages.success(request, 'Kulüp Başarıyla Kayıt Edilmiştir.')

            return redirect('wushu:kulupler')

        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'kulup/kulup-ekle.html',
                  {'club_form': club_form, 'communication_form': communication_form})


@login_required
def return_clubs(request):
    perm = general_methods.control_access(request)


    if not perm:
        logout(request)
        return redirect('accounts:login')
    user = request.user
    clubs = SportsClub.objects.none()
    ClupsSearchForm=ClubSearchForm(request.POST)
    if user.groups.filter(name='KulupUye'):
        clubuser = SportClubUser.objects.get(user=user)
        clubs = SportsClub.objects.filter(clubUser=clubuser)
    if request.method == 'POST':

        if ClupsSearchForm.is_valid():
            kisi = ClupsSearchForm.cleaned_data.get('kisi')
            city = ClupsSearchForm.cleaned_data.get('city')
            name = ClupsSearchForm.cleaned_data.get('name')
            shortName = ClupsSearchForm.cleaned_data.get('shortName')
            clubMail = ClupsSearchForm.cleaned_data.get('clubMail')
            if not (kisi or city or name or shortName or clubMail):
                if user.groups.filter(name='KulupUye'):
                    clubuser = SportClubUser.objects.get(user=user)
                    clubs = SportsClub.objects.filter(clubUser=clubuser)

                elif user.groups.filter(name__in=['Yonetim', 'Admin']):
                    clubs = SportsClub.objects.all()

            else:
                query = Q()
                if city:
                    query &= Q(communication__city__name__icontains=city)
                if name:
                    query &= Q(name__icontains=name)
                if clubMail:
                    query &= Q(clubMail__icontains=clubMail)
                if shortName:
                    query &= Q(shortName__icontains=shortName)
                if kisi:
                    query &= Q(clubUser=kisi)
                if user.groups.filter(name='KulupUye'):
                    clubuser = SportClubUser.objects.get(user=user)
                    clubs = SportsClub.objects.filter(clubUser=clubuser).filter(query)

                elif user.groups.filter(name__in=['Yonetim', 'Admin']):
                    clubs = SportsClub.objects.filter(query)




    return render(request, 'kulup/kulupler.html', {'clubs': clubs,'ClupsSearchForm':ClupsSearchForm})


@login_required
def return_add_club_person(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    user_form = UserForm()
    person_form = PersonForm()
    communication_form = CommunicationForm()
    sportClubUser_form = SportClubUserForm()

    if request.method == 'POST':

        user_form = UserForm(request.POST)
        person_form = PersonForm(request.POST, request.FILES)
        communication_form = CommunicationForm(request.POST, request.FILES)
        sportClubUser_form = SportClubUserForm(request.POST)

        if user_form.is_valid() and person_form.is_valid() and communication_form.is_valid() and sportClubUser_form.is_valid():
            user = User()
            user.username = user_form.cleaned_data['email']
            user.first_name = user_form.cleaned_data['first_name']
            user.last_name = user_form.cleaned_data['last_name']
            user.email = user_form.cleaned_data['email']
            group = Group.objects.get(name='KulupUye')
            password = User.objects.make_random_password()
            user.set_password(password)
            user.save()
            user.groups.add(group)
            user.save()

            person = person_form.save(commit=False)
            communication = communication_form.save(commit=False)
            person.save()
            communication.save()

            club_person = SportClubUser(
                user=user, person=person, communication=communication,
                role=sportClubUser_form.cleaned_data['role'],

            )

            club_person.save()

            subject, from_email, to = 'WUSHU - Kulüp Üye Bilgi Sistemi Kullanıcı Giriş Bilgileri', 'no-reply@twf.gov.tr', user.email
            text_content = 'Aşağıda ki bilgileri kullanarak sisteme giriş yapabilirsiniz.'
            html_content = '<p> <strong>Site adresi: </strong> <a href="http://sbs.twf.gov.tr/"></a>sbs.twf.gov.tr</p>'
            html_content = html_content + '<p><strong>Kullanıcı Adı:  </strong>' + user.username + '</p>'
            html_content = html_content + '<p><strong>Şifre: </strong>' + password + '</p>'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            mesaj = str(user.get_full_name()) + ' klup üyesi  eklendi   '
            log = general_methods.logwrite(request, request.user, mesaj)

            messages.success(request, 'Kulüp Üyesi Başarıyla Kayıt Edilmiştir.')

            return redirect('wushu:kulup-uyeleri')

        else:

            for x in user_form.errors.as_data():
                messages.warning(request, user_form.errors[x][0])

    return render(request, 'kulup/kulup-uyesi-ekle.html',
                  {'user_form': user_form, 'person_form': person_form, 'communication_form': communication_form,
                   'sportClubUser_form': sportClubUser_form,
                   })


@login_required
def updateClubPersons(request, pk):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    athlete = SportClubUser.objects.get(pk=pk)
    user = User.objects.get(pk=athlete.user.pk)
    person = Person.objects.get(pk=athlete.person.pk)
    communication = Communication.objects.get(pk=athlete.communication.pk)
    # sportClub = athlete.sportClub
    user_form = UserForm(request.POST or None, instance=user)
    person_form = PersonForm(request.POST or None, instance=person)
    communication_form = CommunicationForm(request.POST or None, instance=communication)
    sportClubUser_form = SportClubUserForm(request.POST or None, instance=athlete)
    clubs = SportsClub.objects.filter(clubUser__user=user)

    if request.method == 'POST':
        if user_form.is_valid() and communication_form.is_valid() and person_form.is_valid() and sportClubUser_form.is_valid():
            user = user_form.save(commit=False)
            user.username = user_form.cleaned_data['email']
            user.first_name = user_form.cleaned_data['first_name']
            user.last_name = user_form.cleaned_data['last_name']
            user.email = user_form.cleaned_data['email']
            user.save()
            person_form.save()
            communication_form.save()
            sportClubUser_form.save()

            mesaj = str(user.get_full_name()) + ' Klup üyesi güncellenmiştir.   '
            log = general_methods.logwrite(request, request.user, mesaj)




            messages.success(request, 'Kulüp Üyesi Başarıyla Güncellenmiştir.')

            return redirect('wushu:kulup-uyeleri')

        else:

            for x in user_form.errors.as_data():
                messages.warning(request, user_form.errors[x][0])

    return render(request, 'kulup/kulup-uyesi-duzenle.html',
                  {'user_form': user_form, 'communication_form': communication_form,
                   'person_form': person_form, 'sportClubUser_form': sportClubUser_form, 'clubs': clubs})


@login_required
def return_club_person(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')

    user_form = UserSearchForm()
    user = request.user
    club_user_array=SportClubUser.objects.none()
    if user.groups.filter(name='KulupUye'):

        clubuser = SportClubUser.objects.get(user=user)
        clubs = SportsClub.objects.filter(clubUser=clubuser)
        clubsPk = []
        for club in clubs:
            clubsPk.append(club.pk)

        club_user_array = SportClubUser.objects.filter(sportsclub__in=clubsPk).distinct()


    if request.method == 'POST':
        user_form = UserSearchForm(request.POST)
        sportsclup = request.POST.get('sportsClub')




        if user_form.is_valid():
            firstName = user_form.cleaned_data.get('first_name')
            lastName = user_form.cleaned_data.get('last_name')
            email = user_form.cleaned_data.get('email')
            if not (firstName or lastName or email or sportsclup):
                club_user_array = []
                if user.groups.filter(name='KulupUye'):

                    clubuser = SportClubUser.objects.get(user=user)
                    clubs = SportsClub.objects.filter(clubUser=clubuser)
                    clubsPk = []
                    for club in clubs:
                        clubsPk.append(club.pk)

                    club_user_array = SportClubUser.objects.filter(sportsclub__in=clubsPk).distinct()


                elif user.groups.filter(name__in=['Yonetim', 'Admin']):
                    club_user_array = SportClubUser.objects.all()
            else:
                query = Q()
                if lastName:
                    query &= Q(user__last_name__icontains=lastName)
                if firstName:
                    query &= Q(user__first_name__icontains=firstName)
                if email:
                    query &= Q(user__email__icontains=email)
                if sportsclup:
                    query &=Q(sportsclub__name__icontains=sportsclup)

                club_user_array = []
                if user.groups.filter(name='KulupUye'):

                    clubuser = SportClubUser.objects.get(user=user)
                    clubs = SportsClub.objects.filter(clubUser=clubuser)
                    clubsPk = []
                    for club in clubs:
                        clubsPk.append(club.pk)

                    club_user_array = SportClubUser.objects.filter(sportsclub__in=clubsPk).filter(query).distinct()


                elif user.groups.filter(name__in=['Yonetim', 'Admin']):
                    club_user_array = SportClubUser.objects.filter(query).distinct()

    sportclup = SearchClupForm(request.POST, request.FILES or None)
    if user.groups.filter(name='KulupUye'):
        sc_user = SportClubUser.objects.get(user=user)
        clubs = SportsClub.objects.filter(clubUser=sc_user)
        clubsPk = []
        for club in clubs:
            clubsPk.append(club.pk)
        sportclup.fields['sportsClub'].queryset = SportsClub.objects.filter(id__in=clubsPk)
    elif user.groups.filter(name__in=['Yonetim', 'Admin']):
        sportclup.fields['sportsClub'].queryset = SportsClub.objects.all()

    return render(request, 'kulup/kulup-uyeleri.html', {'athletes': club_user_array, 'user_form': user_form,'Sportclup':sportclup})


@login_required
def return_club_role(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    club_role_form = ClubRoleForm()

    if request.method == 'POST':

        club_role_form = ClubRoleForm(request.POST)

        if club_role_form.is_valid():

            clubrole = ClubRole(name=club_role_form.cleaned_data['name'])
            clubrole.save()
            messages.success(request, 'Kulüp Üye Rolü Başarıyla Kayıt Edilmiştir.')
            return redirect('wushu:kulup-uye-rolu')

        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')
    club_role = ClubRole.objects.all()
    return render(request, 'kulup/kulup-uye-rolu.html',
                  {'club_role_form': club_role_form, 'club_role': club_role})


@login_required
def deleteClubRole(request, pk):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    if request.method == 'POST' and request.is_ajax():
        try:
            obj = ClubRole.objects.get(pk=pk)
            obj.delete()
            return JsonResponse({'status': 'Success', 'messages': 'save successfully'})
        except ClubRole.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})


@login_required
def deleteClubUser(request, pk):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    if request.method == 'POST' and request.is_ajax():
        try:
            obj = SportClubUser.objects.get(pk=pk)
            obj.delete()
            return JsonResponse({'status': 'Success', 'messages': 'delete successfully'})
        except ClubRole.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})


@login_required
def deleteClubUserFromClub(request, pk, club_pk):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    if request.method == 'POST' and request.is_ajax():
        try:
            obj = SportClubUser.objects.get(pk=pk)
            club = SportsClub.objects.get(pk=club_pk)

            club.clubUser.remove(obj)
            club.save()

            return JsonResponse({'status': 'Success', 'messages': 'delete successfully'})
        except ClubRole.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})


@login_required
def deleteCoachFromClub(request, pk, club_pk):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    if request.method == 'POST' and request.is_ajax():
        try:
            obj = Coach.objects.get(pk=pk)
            club = SportsClub.objects.get(pk=club_pk)

            club.coachs.remove(obj)
            club.save()

            return JsonResponse({'status': 'Success', 'messages': 'delete successfully'})
        except ClubRole.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})


@login_required
def updateClubRole(request, pk):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    clubrole = ClubRole.objects.get(id=pk)
    clubrole_form = ClubRoleForm(request.POST or None, instance=clubrole)

    if request.method == 'POST':
        if clubrole_form.is_valid():
            clubrole_form.save()
            messages.success(request, 'Başarıyla Güncellendi')
            return redirect('wushu:kulup-uye-rolu')
        else:
            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'kulup/kulupRolDuzenle.html',
                  {'clubrole_form': clubrole_form})


@login_required
def clubDelete(request, pk):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    if request.method == 'POST' and request.is_ajax():
        try:
            obj = SportsClub.objects.get(pk=pk)
            obj.delete()
            return JsonResponse({'status': 'Success', 'messages': 'save successfully'})
        except SportsClub.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})


@login_required
def clubUpdate(request, pk):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    club = SportsClub.objects.get(pk=pk)
    com_id = club.communication.pk
    communication = Communication.objects.get(id=com_id)
    club_form = ClubForm(request.POST or None, instance=club)
    communication_form = CommunicationForm(request.POST or None, instance=communication)
    clubPersons = club.clubUser.all()

    clubCoachs = club.coachs.all()

    if request.method == 'POST':
        if club_form.is_valid():
            club_form.save()
            communication_form.save()

            mesaj = str(club.name) + ' klüp güncellendi  '
            log = general_methods.logwrite(request, request.user, mesaj)


            messages.success(request, 'Başarıyla Güncellendi')
            return redirect('wushu:kulupler')
        else:
            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'kulup/kulupDuzenle.html',
                  {'club_form': club_form, 'communication_form': communication_form, 'clubPersons': clubPersons,
                   'club': club, 'clubCoachs': clubCoachs})


@login_required
def choose_coach(request, pk):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    coaches = Coach.objects.all()
    user_form = UserSearchForm()
    if request.method == 'POST':

        if user_form.is_valid():
            firstName = user_form.cleaned_data.get('first_name')
            lastName = user_form.cleaned_data.get('last_name')
            email = user_form.cleaned_data.get('email')
            if not (firstName or lastName or email):
                messages.warning(request, 'Lütfen Arama Kriteri Giriniz.')
            else:
                query = Q()
                if lastName:
                    query &= Q(user__last_name__icontains=lastName)
                if firstName:
                    query &= Q(user__first_name__icontains=firstName)
                if email:
                    query &= Q(user__email__icontains=email)
                coaches = Coach.objects.filter(query)
        user_form = UserSearchForm(request.POST)
        athletes1 = request.POST.getlist('selected_options')
        if athletes1:
            students = [int(x) for x in athletes1]
            instances = Coach.objects.filter(id__in=students)
            club = SportsClub.objects.get(pk=pk)
            for coach in instances:
                club.coachs.add(coach)
            club.save()
            messages.success(request, 'Antrenör Başarıyla Eklenmiştir.')

            return redirect('wushu:update-club', pk=pk)

    return render(request, 'antrenor/antrenorsec.html', {'coaches': coaches, 'user_form': user_form})


@login_required
def choose_sport_club_user(request, pk):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    sportClubUsers = SportClubUser.objects.all()
    user_form = UserSearchForm()
    if request.method == 'POST':
        user_form = UserSearchForm(request.POST)
        athletes1 = request.POST.getlist('selected_options')
        if user_form.is_valid():
            firstName = user_form.cleaned_data.get('first_name')
            lastName = user_form.cleaned_data.get('last_name')
            email = user_form.cleaned_data.get('email')
            if not (firstName or lastName or email):
                print("asasa")
                # messages.warning(request, 'Lütfen Arama Kriteri Giriniz.')
            else:
                query = Q()
                if lastName:
                    query &= Q(user__last_name__icontains=lastName)
                if firstName:
                    query &= Q(user__first_name__icontains=firstName)
                if email:
                    query &= Q(user__email__icontains=email)
                sportClubUsers = SportClubUser.objects.filter(query)
        if athletes1:
            students = [int(x) for x in athletes1]
            instances = SportClubUser.objects.filter(id__in=students)

            club = SportsClub.objects.get(pk=pk)
            for club_user in instances:
                club.clubUser.add(club_user)

                mesaj = str(club_user.user.get_full_name()) + ' klup üyesi eklendi  ' + str(club.name)
                log = general_methods.logwrite(request, request.user, mesaj)



            club.save()

            messages.success(request, 'Kulüp Üyesi Başarıyla Eklenmiştir.')

            return redirect('wushu:update-club', pk=pk)

    return render(request, 'kulup/kulupuyesisec.html', {'coaches': sportClubUsers, 'user_form': user_form})


@login_required
def return_belt_exams(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')

    user = request.user

    if user.groups.filter(name='KulupUye'):

        clubuser = SportClubUser.objects.get(user=user)
        clubs = SportsClub.objects.filter(clubUser=clubuser)
        clubsPk = []
        for club in clubs:
            clubsPk.append(club.pk)

        exams = BeltExam.objects.filter(sportClub__in=clubsPk)


    elif user.groups.filter(name__in=['Yonetim', 'Admin']):
        exams = BeltExam.objects.all()

    if int(timezone.now().month) % 3 == 0:
        examMonth = True
    else:
        examMonth = False

    print(examMonth)

    return render(request, 'kulup/kusak-sinavlari.html', {'exams': exams, 'examMonth': examMonth})


def detail_belt_exam(request, pk):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    exam = BeltExam.objects.get(pk=pk)
    return render(request, 'kulup/kusak-sinavi-incele.html', {'exam': exam})


@login_required
def approve_belt_exam(request, pk):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    exam = BeltExam.objects.get(pk=pk)
    # her onaya geldiginde kuşaklari bir üst seviyeye göndermesini engelledik.
    if exam.status!=BeltExam.APPROVED:
        athletes = exam.athletes.all()
        for athlete in athletes:
            level = Level()
            level.startDate = exam.examDate
            level.levelType = EnumFields.LEVELTYPE.BELT

            lastLevel = Level.objects.get(branch=exam.branch, isActive=True)
            lastDefinition = lastLevel.definition
            level.definition = lastDefinition.parent
            level.status = Level.APPROVED
            level.isActive = True
            level.save()

            for item in athlete.belts.all():
                if item.branch == exam.branch:
                    item.isActive = False
                    item.save()

            athlete.belts.add(level)
            athlete.save()

    exam.status = BeltExam.APPROVED
    exam.save()
    messages.success(request, 'Sınav Onaylanmıştır.')
    return redirect('wushu:kusak-sinavi-incele', pk=pk)


def denied_belt_exam(request, pk):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    exam = BeltExam.objects.get(pk=pk)
    exam.status = exam.DENIED
    exam.save()
    return redirect('wushu:kusak-sinavi-incele', pk=pk)


# sporcu seç
@login_required
def choose_athlete(request, pk):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    login_user = request.user
    user = User.objects.get(pk=login_user.pk)
    sinav = BeltExam.objects.get(pk=pk)
    if user.groups.filter(name='KulupUye'):
        sc_user = SportClubUser.objects.get(user=user)
        clubsPk = []
        clubs = SportsClub.objects.filter(clubUser=sc_user)
        for club in clubs:
            clubsPk.append(club.pk)
        exam_athlete = []
        for item in sinav.athletes.all():
            exam_athlete.append(item.user.pk)
        athletes = Athlete.objects.filter(licenses__sportsClub__in=clubsPk).exclude(belts=None).exclude(licenses=None).exclude(beltexam__athletes__user__in = exam_athlete).filter(licenses__branch=sinav.branch,licenses__status='Onaylandı').filter(belts__branch=sinav.branch,belts__status='Onaylandı').distinct()
    elif user.groups.filter(name__in=['Yonetim', 'Admin']):
        exam_athlete=[]
        for item in sinav.athletes.all():
            exam_athlete.append(item.user.pk)
        print(sinav.branch)
        athletes=Athlete.objects.exclude(belts=None).exclude(licenses=None).exclude(beltexam__athletes__user__in = exam_athlete).filter(licenses__branch=sinav.branch,licenses__status='Onaylandı').filter(belts__branch=sinav.branch,belts__status='Onaylandı')
    #   .exclude(belts__definition__parent_id=None)    eklenmeli ama eklendigi zaman kuşaklarindan bir tanesi en üst olunca almıyor
    if request.method == 'POST':

        athletes1 = request.POST.getlist('selected_options')
        if athletes1:
            for x in athletes1:
                sinav.athletes.add(x)
        return redirect('wushu:kusak-sinavi-incele', pk=pk)
    return render(request, 'kulup/kusak-sınavı-antroner-sec.html', {'athletes': athletes})


@login_required
def choose_coach(request, pk):
    perm = general_methods.control_access(request)
    if not perm:
        logout(request)
        return redirect('accounts:login')
    login_user = request.user
    user = User.objects.get(pk=login_user.pk)
    sinav = BeltExam.objects.get(pk=pk)
    athletes = Coach.objects.none()
    # .filter(grades__branch=sinav.branch) eklenmeli
    coa=[]
    for item in sinav.coachs.all():
        coa.append(item.user.pk)
    athletes = Coach.objects.filter(grades__branch=sinav.branch,grades__status='Onaylandı').exclude(beltexam__coachs__user_id__in=coa).filter(visa__startDate__year=timezone.now().year).exclude(grades=None).exclude(visa=None).exclude(grades__definition__name='1.Kademe').exclude(grades__definition=None).distinct()
    # for fd in coach:
    #     for visa in fd.visa.all():
    #         if(date(sinav.examDate.year,sinav.examDate.month,sinav.examDate.day)-date(visa.creationDate.year,visa.creationDate.month,visa.creationDate.day)).days<365:
    #             athletes|=Coach.objects.filter(pk=fd.pk).distinct()

    if request.method == 'POST':
        athletes1 = request.POST.getlist('selected_options')
        if athletes1:
            for x in athletes1:
                if  not sinav.coachs.all().filter(beltexam__coachs__user_id=x):
                    sinav.coachs.add(x)
                    sinav.save()
        return redirect('wushu:kusak-sinavi-incele', pk=pk)
    return render(request, 'kulup/kusak-sınavı-antroner-sec.html', {'athletes': athletes})


@login_required
def add_belt_exam(request):
    perm = general_methods.control_access(request),
    if not perm:
        logout(request)
        return redirect('accounts:login')
    exam_form = BeltExamForm(request.POST, request.FILES or None)
    user = request.user
    if user.groups.filter(name='KulupUye'):
        sc_user = SportClubUser.objects.get(user=user)
        clubs = SportsClub.objects.filter(clubUser=sc_user)
        clubsPk = []
        for club in clubs:
            clubsPk.append(club.pk)
        exam_form.fields['sportClub'].queryset = SportsClub.objects.filter(id__in=clubsPk)


    elif user.groups.filter(name__in=['Yonetim', 'Admin']):
        exam_form.fields['sportClub'].queryset = SportsClub.objects.all()

    if request.method == 'POST':
        exam_form = BeltExamForm(request.POST, request.FILES or None)
        if exam_form.is_valid():
            exam = exam_form.save()
            messages.success(request, 'Sınav başarıyla oluşturuldu')
            return redirect('wushu:kusak-sinavlari')
        else:
            messages.warning(request, 'Alanları Kontrol Ediniz')
    return render(request, 'kulup/kusak-sinavi-ekle.html', {'exam_form': exam_form})


@login_required
def update_belt_exam(request, pk):
    print('kusak sinavi düzenle çalisti')
    perm = general_methods.control_access(request)
    if not perm:
        logout(request)
        return redirect('accounts:login')
    sinav = BeltExam.objects.get(pk=pk)
    exam_form = BeltExamForm(request.POST or None, request.FILES or None, instance=sinav,
                             initial={'sportClub': sinav.sportClub, 'dekont': sinav.dekont})
    user = request.user
    if user.groups.filter(name='KulupUye'):
        sc_user = SportClubUser.objects.get(user=user)
        clubs = SportsClub.objects.filter(clubUser=sc_user)
        clubsPk = []
        for club in clubs:
            clubsPk.append(club.pk)
        exam_form.fields['sportClub'].queryset = SportsClub.objects.filter(id__in=clubsPk)


    elif user.groups.filter(name__in=['Yonetim', 'Admin']):
        exam_form.fields['sportClub'].queryset = SportsClub.objects.all()

    if request.method == 'POST':
        if exam_form.is_valid():
            exam = exam_form.save()
            messages.success(request, 'Sınav başarıyla güncellendi')
            return redirect('wushu:kusak-sinavi-incele', pk=pk)
        else:
            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'kulup/kusak-sinavi-güncelle.html', {'exam_form': exam_form})


@login_required
def delete_belt_exam(request, pk):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    if request.method == 'POST' and request.is_ajax():
        try:
            obj = SportsClub.objects.get(pk=pk)
            obj.delete()
            return JsonResponse({'status': 'Success', 'messages': 'save successfully'})
        except SportsClub.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})


@login_required
def updateClubPersonsProfile(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')

    user = request.user
    club_user = SportClubUser.objects.get(user=user)
    person = Person.objects.get(pk=club_user.person.pk)
    communication = Communication.objects.get(pk=club_user.communication.pk)
    user_form = DisabledUserForm(request.POST or None, instance=user)
    person_form = DisabledPersonForm(request.POST or None, request.FILES or None, instance=person)
    communication_form = DisabledCommunicationForm(request.POST or None, instance=communication)
    club_form = DisabledSportClubUserForm(request.POST or None, instance=club_user)
    password_form = SetPasswordForm(request.user, request.POST)

    if request.method == 'POST':
        data = request.POST.copy()
        data['bloodType'] = "AB Rh+"
        data['gender'] = "Erkek"
        person_form = DisabledPersonForm(data)

        if person_form.is_valid() and password_form.is_valid():
            if len(request.FILES) > 0:
                person.profileImage = request.FILES['profileImage']
                person.save()
                messages.success(request, 'Profil Fotoğrafı Başarıyla Güncellenmiştir.')

            user.set_password(password_form.cleaned_data['new_password2'])
            user.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Şifre Başarıyla Güncellenmiştir.')
            return redirect('wushu:kulup-uyesi-profil-guncelle')



        elif person_form.is_valid() and not password_form.is_valid():
            if len(request.FILES) > 0:
                person.profileImage = request.FILES['profileImage']
                person.save()
                messages.success(request, 'Profil Fotoğrafı Başarıyla Güncellenmiştir.')
            else:
                messages.warning(request, 'Alanları Kontrol Ediniz')
            return redirect('wushu:kulup-uyesi-profil-guncelle')


        elif not person_form.is_valid() and password_form.is_valid():
            user.set_password(password_form.cleaned_data['new_password2'])
            user.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Şifre Başarıyla Güncellenmiştir.')
            return redirect('wushu:kulup-uyesi-profil-guncelle')

        else:
            messages.warning(request, 'Alanları Kontrol Ediniz.')

            return redirect('wushu:kulup-uyesi-profil-guncelle')

    return render(request, 'kulup/kulup-uyesi-profil-guncelle.html',
                  {'user_form': user_form, 'communication_form': communication_form,
                   'person_form': person_form, 'password_form': password_form, 'club_form': club_form})


@login_required
def Exam_list_antroner_delete(request, pk):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    if request.method == 'POST' and request.is_ajax():
        try:
            obj = SportsClub.objects.get(pk=pk)
            obj.delete()
            return JsonResponse({'status': 'Success', 'messages': 'save successfully'})
        except SportsClub.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})


# listeden antroner sil

@login_required
def choose_coach_remove(request, pk, exam_pk):
    perm = general_methods.control_access_klup(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')

    sinav = BeltExam.objects.get(pk=exam_pk)
    sinav.coachs.remove(Coach.objects.get(pk=pk))

    return redirect('wushu:kusak-sinavi-incele', pk=exam_pk)


@login_required
def choose_athlete_remove(request, pk, exam_pk):
    perm = general_methods.control_access_klup(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')

    sinav = BeltExam.objects.get(pk=exam_pk)
    sinav.athletes.remove(Athlete.objects.get(pk=pk))

    return redirect('wushu:kusak-sinavi-incele', pk=exam_pk)
