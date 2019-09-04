from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from wushu.Forms.CommunicationForm import CommunicationForm
from wushu.Forms.DirectoryCommissionForm import DirectoryCommissionForm
from wushu.Forms.DirectoryMemberRoleForm import DirectoryMemberRoleForm
from wushu.Forms.UserForm import UserForm
from wushu.Forms.PersonForm import PersonForm
from wushu.Forms.UserSearchForm import UserSearchForm
from wushu.models import Person, Communication
from wushu.models.DirectoryCommission import DirectoryCommission
from wushu.models.DirectoryMember import DirectoryMember
from wushu.models.DirectoryMemberRole import DirectoryMemberRole


@login_required
def add_directory_member(request):
    user_form = UserForm()
    person_form = PersonForm()
    communication_form = CommunicationForm()

    if request.method == 'POST':

        user_form = UserForm(request.POST)
        person_form = PersonForm(request.POST, request.FILES)
        communication_form = CommunicationForm(request.POST)

        if user_form.is_valid() and person_form.is_valid() and communication_form.is_valid():
            user = User()
            user.username = user_form.cleaned_data['email']
            user.first_name = user_form.cleaned_data['first_name']
            user.last_name = user_form.cleaned_data['last_name']
            user.email = user_form.cleaned_data['email']
            group = Group.objects.get(name='Antrenor')
            password = User.objects.make_random_password()
            user.set_password(password)
            user.save()
            user.groups.add(group)
            user.save()

            person = person_form.save(commit=False)
            communication = communication_form.save(commit=False)
            person.save()
            communication.save()

            directoryMember = DirectoryMember(user=user, person=person, communication=communication)

            directoryMember.save()

            subject, from_email, to = 'WUSHU - Antrenör Bilgi Sistemi Kullanıcı Giriş Bilgileri', 'kayit@oxityazilim.com', user.email
            text_content = 'Aşağıda ki bilgileri kullanarak sisteme giriş yapabilirsiniz.'
            html_content = '<p> <strong>Site adresi: </strong> <a href="https://www.twf.gov.tr/"></a>https://www.twf.gov.tr/</p>'
            html_content = html_content + '<p><strong>Kullanıcı Adı:  </strong>' + user.username + '</p>'
            html_content = html_content + '<p><strong>Şifre: </strong>' + password + '</p>'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            messages.success(request, 'Yönetim Kurulu Üyesi Başarıyla Kayıt Edilmiştir.')

            return redirect('wushu:kurul-uyeleri')

        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'yonetim/kurul-uyesi-ekle.html',
                  {'user_form': user_form, 'person_form': person_form, 'communication_form': communication_form})


@login_required
def return_directory_members(request):
    members = DirectoryMember.objects.all()
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
                members = DirectoryMember.objects.filter(query)
    return render(request, 'yonetim/kurul-uyeleri.html', {'members': members, 'user_form': user_form})


@login_required
def delete_directory_member(request, pk):
    if request.method == 'POST' and request.is_ajax():
        try:
            obj = DirectoryMember.objects.get(pk=pk)
            obj.delete()
            return JsonResponse({'status': 'Success', 'messages': 'save successfully'})
        except DirectoryMember.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})


@login_required
def update_directory_member(request, pk):
    member = DirectoryMember.objects.get(pk=pk)
    user = User.objects.get(pk=member.user.pk)
    person = Person.objects.get(pk=member.person.pk)
    communication = Communication.objects.get(pk=member.communication.pk)
    user_form = UserForm(request.POST or None, instance=user)
    person_form = PersonForm(request.POST or None, instance=person)
    communication_form = CommunicationForm(request.POST or None, instance=communication)
    if request.method == 'POST':
        if user_form.is_valid() and person_form.is_valid() and communication_form.is_valid():

            user.username = user_form.cleaned_data['email']
            user.first_name = user_form.cleaned_data['first_name']
            user.last_name = user_form.cleaned_data['last_name']
            user.email = user_form.cleaned_data['email']
            user.save()
            person_form.save()
            communication_form.save()

            messages.success(request, 'Yönetim Kurulu Üyesi Başarıyla Güncellendi')
            return redirect('wushu:kurul-uyeleri')
        else:
            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'yonetim/kurul-uyesi-duzenle.html',
                  {'user_form': user_form, 'communication_form': communication_form,
                   'person_form': person_form})


login_required


def return_member_roles(request):
    member_role_form = DirectoryMemberRoleForm();

    if request.method == 'POST':

        member_role_form = DirectoryMemberRoleForm(request.POST)

        if member_role_form.is_valid():

            memberRole = DirectoryMemberRole(name=member_role_form.cleaned_data['name'])
            memberRole.save()
            messages.success(request, 'Kurul Üye Rolü Başarıyla Kayıt Edilmiştir.')
            return redirect('wushu:kurul-uye-rolleri')

        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')
    memberRoles = DirectoryMemberRole.objects.all()
    return render(request, 'yonetim/kurul-uye-rolleri.html',
                  {'member_role_form': member_role_form, 'memberRoles': memberRoles})


@login_required
def delete_member_role(request, pk):
    if request.method == 'POST' and request.is_ajax():
        try:
            obj = DirectoryMemberRole.objects.get(pk=pk)
            obj.delete()
            return JsonResponse({'status': 'Success', 'messages': 'save successfully'})
        except DirectoryMemberRole.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})


@login_required
def update_member_role(request, pk):
    memberRole = DirectoryMemberRole.objects.get(id=pk)
    member_role_form = DirectoryMemberRoleForm(request.POST or None, instance=memberRole)

    if request.method == 'POST':
        if member_role_form.is_valid():
            member_role_form.save()
            messages.success(request, 'Başarıyla Güncellendi')
            return redirect('wushu:kurul-uye-rolleri')
        else:
            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'yonetim/kurul_uye_rol_duzenle.html',
                  {'member_role_form': member_role_form})


@login_required
def return_commissions(request):
    commission_form = DirectoryCommissionForm();

    if request.method == 'POST':

        commission_form = DirectoryCommissionForm(request.POST)

        if commission_form.is_valid():

            commission = DirectoryCommission(name=commission_form.cleaned_data['name'])
            commission.save()
            messages.success(request, 'Kurul Başarıyla Kayıt Edilmiştir.')
            return redirect('wushu:kurullar')

        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')
    commissions = DirectoryCommission.objects.all()
    return render(request, 'yonetim/kurullar.html',
                  {'commission_form': commission_form, 'commissions': commissions})


@login_required
def delete_commission(request, pk):
    if request.method == 'POST' and request.is_ajax():
        try:
            obj = DirectoryCommission.objects.get(pk=pk)
            obj.delete()
            return JsonResponse({'status': 'Success', 'messages': 'save successfully'})
        except DirectoryCommission.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})


@login_required
def update_commission(request, pk):
    commission = DirectoryCommission.objects.get(id=pk)
    commission_form = DirectoryCommissionForm(request.POST or None, instance=commission)

    if request.method == 'POST':
        if commission_form.is_valid():
            commission_form.save()
            messages.success(request, 'Başarıyla Güncellendi')
            return redirect('wushu:kurullar')
        else:
            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'yonetim/kurul_duzenle.html',
                  {'commission_form': commission_form})
