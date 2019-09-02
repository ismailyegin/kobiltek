from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from wushu.Forms.ClubForm import ClubForm
from wushu.Forms.ClubRoleForm import ClubRoleForm
from wushu.Forms.CommunicationForm import CommunicationForm
from wushu.Forms.PersonForm import PersonForm
from wushu.Forms.SportClubUserForm import SportClubUserForm
from wushu.Forms.UserForm import UserForm
from wushu.Forms.UserSearchForm import UserSearchForm
from wushu.models import SportsClub, SportClubUser, Communication, Person
from wushu.models.ClubRole import ClubRole


@login_required
def return_add_club(request):
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
                                  clubMail=club_form.cleaned_data['clubMail']

                                  )

            communication = communication_form.save(commit=False)
            communication.save()
            clubsave.communication = communication

            clubsave.save()

            messages.success(request, 'Kulüp Başarıyla Kayıt Edilmiştir.')

            return redirect('wushu:kulupler')

        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'kulup/kulup-ekle.html',
                  {'club_form': club_form, 'communication_form': communication_form})


@login_required
def return_clubs(request):
    clubs = SportsClub.objects.all()

    return render(request, 'kulup/kulupler.html', {'clubs': clubs})


@login_required
def return_add_club_person(request, pk):
    user_form = UserForm()
    person_form = PersonForm()
    communication_form = CommunicationForm()
    sportClubUser_form = SportClubUserForm()

    sportClub = SportsClub.objects.get(pk=pk)

    if request.method == 'POST':

        data = request.POST.copy()
        data['username'] = data['email']
        user_form = UserForm(data)
        person_form = PersonForm(request.POST, request.FILES)
        communication_form = CommunicationForm(request.POST, request.FILES)
        sportClubUser_form = SportClubUserForm(request.POST)

        if user_form.is_valid() and person_form.is_valid() and communication_form.is_valid() and sportClubUser_form.is_valid():
            user = user_form.save(commit=False)
            person = person_form.save(commit=False)
            communication = communication_form.save(commit=False)

            group = Group.objects.get(name='Kulüp Üyesi')
            user2 = user_form.save()
            password = User.objects.make_random_password()
            user.set_password(password)
            user2.groups.add(group)

            user.save()
            person.save()
            communication.save()

            club_person = SportClubUser(
                user=user, person=person, communication=communication,
                role=sportClubUser_form.cleaned_data['role'],
                sportClub=sportClub

            )

            club_person.save()

            subject, from_email, to = 'WUSHU - Sporcu Bilgi Sistemi Kullanıcı Giriş Bilgileri', 'kayit@oxityazilim.com', user2.email
            text_content = 'Aşağıda ki bilgileri kullanarak sisteme giriş yapabilirsiniz.'
            html_content = '<p> <strong>Site adresi: </strong> <a href="https://www.twf.gov.tr/"></a>https://www.twf.gov.tr/</p>'
            html_content = html_content + '<p><strong>Kullanıcı Adı:  </strong>' + user2.username + '</p>'
            html_content = html_content + '<p><strong>Şifre: </strong>' + password + '</p>'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            messages.success(request, 'Kulüp Üyesi Başarıyla Kayıt Edilmiştir.')

            return redirect('wushu:update-club', pk=pk)

        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'kulup/kulup-uyesi-ekle.html',
                  {'user_form': user_form, 'person_form': person_form, 'communication_form': communication_form,
                   'sportClubUser_form': sportClubUser_form,
                   })


@login_required
def updateClubPersons(request, pk):
    athlete = SportClubUser.objects.get(pk=pk)
    user = User.objects.get(pk=athlete.user.pk)
    person = Person.objects.get(pk=athlete.person.pk)
    communication = Communication.objects.get(pk=athlete.communication.pk)
    sportClub = athlete.sportClub
    user_form = UserForm(request.POST or None, instance=user)
    person_form = PersonForm(request.POST or None, instance=person)
    communication_form = CommunicationForm(request.POST or None, instance=communication)
    sportClubUser_form = SportClubUserForm(request.POST or None, instance=athlete)

    if request.method == 'POST':

        if user_form.is_valid() and communication_form.is_valid() and person_form.is_valid() and sportClubUser_form.is_valid():

            user = User()
            user.username = user_form.cleaned_data['email']
            user.first_name = user_form.cleaned_data['first_name']
            user.last_name = user_form.cleaned_data['last_name']
            user.email = user_form.cleaned_data['email']
            user.save()
            person_form.save()
            communication_form.save()
            sportClubUser_form.save()

            messages.success(request, 'Kulüp Üyesi Başarıyla Güncellenmiştir.')

            return redirect('wushu:update-club', pk=sportClub.pk)

        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'kulup/kulup-uyesi-duzenle.html',
                  {'user_form': user_form, 'communication_form': communication_form,
                   'person_form': person_form, 'sportClubUser_form': sportClubUser_form})


@login_required
def return_club_person(request):
    athletes = SportClubUser.objects.all()
    user_form = UserSearchForm()

    if request.method == 'POST':
        user_form = UserSearchForm(request.POST)
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
                athletes = SportClubUser.objects.filter(query)

    return render(request, 'kulup/kulup-uyeleri.html', {'athletes': athletes, 'user_form': user_form})


@login_required
def return_club_role(request):
    club_role_form = ClubRoleForm();

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
def updateClubRole(request, pk):
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
    club = SportsClub.objects.get(id=pk)
    com_id = club.communication.pk
    communication = Communication.objects.get(id=com_id)
    club_form = ClubForm(request.POST or None, instance=club)
    communication_form = CommunicationForm(request.POST or None, instance=communication)
    clubPersons = SportClubUser.objects.filter(sportClub=club)

    if request.method == 'POST':
        if club_form.is_valid():
            club_form.save()
            communication_form.save()
            messages.success(request, 'Başarıyla Güncellendi')
            return redirect('wushu:kulupler')
        else:
            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'kulup/kulupDuzenle.html',
                  {'club_form': club_form, 'communication_form': communication_form, 'clubPersons': clubPersons,
                   'club': club})
