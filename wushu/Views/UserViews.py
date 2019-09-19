from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from wushu.Forms.CommunicationForm import CommunicationForm
from wushu.Forms.DirectoryCommissionForm import DirectoryCommissionForm
from wushu.Forms.DirectoryForm import DirectoryForm
from wushu.Forms.DirectoryMemberRoleForm import DirectoryMemberRoleForm
from wushu.Forms.DisabledCommunicationForm import DisabledCommunicationForm
from wushu.Forms.DisabledPersonForm import DisabledPersonForm
from wushu.Forms.DisabledSportClubUserForm import DisabledSportClubUserForm
from wushu.Forms.DisabledUserForm import DisabledUserForm
from wushu.Forms.SportClubUserForm import SportClubUserForm
from wushu.Forms.UserForm import UserForm
from wushu.Forms.PersonForm import PersonForm
from wushu.Forms.UserSearchForm import UserSearchForm
from wushu.models import Person, Communication, SportClubUser
from wushu.models.DirectoryCommission import DirectoryCommission
from wushu.models.DirectoryMember import DirectoryMember
from wushu.models.DirectoryMemberRole import DirectoryMemberRole


@login_required
def return_users(request):
    users = User.objects.all()
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
                    query &= Q(last_name__icontains=lastName)
                if firstName:
                    query &= Q(first_name__icontains=firstName)
                if email:
                    query &= Q(email__icontains=email)
                print(query)
                users = User.objects.filter(query)
    return render(request, 'kullanici/kullanicilar.html', {'users': users, 'user_form': user_form})


@login_required
def update_user(request, pk):
    user = User.objects.get(pk=pk)
    club_user = SportClubUser.objects.get(user=user)
    person = Person.objects.get(pk=club_user.person.pk)
    communication = Communication.objects.get(pk=club_user.communication.pk)


    user_form = DisabledUserForm(request.POST or None, instance=user)
    person_form = DisabledPersonForm(request.POST or None, instance=person)
    communication_form = DisabledCommunicationForm(request.POST or None, instance=communication)
    club_form = DisabledSportClubUserForm(request.POST or None, instance=club_user)
    password_form = SetPasswordForm(request.user, request.POST)

    if request.method == 'POST':

        if user_form.is_valid() and communication_form.is_valid() and person_form.is_valid() and password_form.is_valid() and club_form.is_valid():

            user.username = user_form.cleaned_data['email']
            user.first_name = user_form.cleaned_data['first_name']
            user.last_name = user_form.cleaned_data['last_name']
            user.email = user_form.cleaned_data['email']
            user.set_password(password_form.cleaned_data['new_password1'])
            user.save()

            person_form.save()
            communication_form.save()
            club_form.save()
            password_form.save()

            update_session_auth_hash(request, user)
            messages.success(request, 'Kullanıcı Başarıyla Güncellendi')
            return redirect('wushu:kullanicilar')
        else:
            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'kullanici/kullanici-duzenle.html',
                  {'user_form': user_form, 'person_form': person_form, 'communication_form': communication_form,
                   'password_form': password_form, 'club_form':club_form})


@login_required
def active_user(request, pk):
    if request.method == 'POST' and request.is_ajax():

        obj = User.objects.get(pk=pk)
        if obj.is_active:
            obj.is_active = False
            obj.save()
        else:
            obj.is_active = True
            obj.save()
        print(obj.is_active)
        return JsonResponse({'status': 'Success', 'messages': 'save successfully'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})
