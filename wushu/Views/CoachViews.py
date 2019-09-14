from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from wushu.Forms.CategoryItemForm import CategoryItemForm
from wushu.Forms.CommunicationForm import CommunicationForm
from wushu.Forms.UserForm import UserForm
from wushu.Forms.PersonForm import PersonForm
from wushu.Forms.UserSearchForm import UserSearchForm
from wushu.models import Coach, CategoryItem, Athlete, Person, Communication, SportClubUser


@login_required
def return_add_coach(request):
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

            coach = Coach(user=user, person=person, communication=communication)

            coach.save()

            subject, from_email, to = 'WUSHU - Antrenör Bilgi Sistemi Kullanıcı Giriş Bilgileri', 'kayit@oxityazilim.com', user.email
            text_content = 'Aşağıda ki bilgileri kullanarak sisteme giriş yapabilirsiniz.'
            html_content = '<p> <strong>Site adresi: </strong> <a href="https://www.twf.gov.tr/"></a>https://www.twf.gov.tr/</p>'
            html_content = html_content + '<p><strong>Kullanıcı Adı:  </strong>' + user.username + '</p>'
            html_content = html_content + '<p><strong>Şifre: </strong>' + password + '</p>'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            messages.success(request, 'Antrenör Başarıyla Kayıt Edilmiştir.')

            return redirect('wushu:antrenorler')

        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'antrenor/antrenor-ekle.html',
                  {'user_form': user_form, 'person_form': person_form, 'communication_form': communication_form})


@login_required
def return_coachs(request):
    coachs = Coach.objects.all()
    login_user = request.user
    user = User.objects.get(pk=login_user.pk)
    if user.groups.filter(name='KulupUye'):
        sc_user = SportClubUser.objects.get(user=user)
        coachs = Coach.objects.filter(sportsclub=sc_user.sportClub)
    elif user.groups.filter(name__in=['Yonetim', 'Admin']):
        coachs = Coach.objects.all()
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
                coachs = Coach.objects.filter(query)
    return render(request, 'antrenor/antrenorler.html', {'coachs': coachs, 'user_form': user_form})


@login_required
def return_grade(request):
    category_item_form = CategoryItemForm();

    if request.method == 'POST':

        category_item_form = CategoryItemForm(request.POST)

        if category_item_form.is_valid():

            categoryItem = CategoryItem(name=category_item_form.cleaned_data['name'])
            categoryItem.forWhichClazz = "GRADE"
            categoryItem.save()

            return redirect('wushu:kademe')

        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')
    categoryitem = CategoryItem.objects.filter(forWhichClazz="GRADE")
    return render(request, 'antrenor/kademe.html',
                  {'category_item_form': category_item_form, 'categoryitem': categoryitem})


@login_required
def categoryItemDelete(request, pk):
    if request.method == 'POST' and request.is_ajax():
        try:
            obj = CategoryItem.objects.get(pk=pk)
            obj.delete()
            return JsonResponse({'status': 'Success', 'messages': 'save successfully'})
        except CategoryItem.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})


@login_required
def categoryItemUpdate(request, pk):
    categoryItem = CategoryItem.objects.get(id=pk)
    category_item_form = CategoryItemForm(request.POST or None, instance=categoryItem)
    if request.method == 'POST':
        if category_item_form.is_valid():
            category_item_form.save()
            messages.warning(request, 'Başarıyla Güncellendi')
            return redirect('wushu:kademe')
        else:
            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'antrenor/kademeDuzenle.html',
                  {'category_item_form': category_item_form})


@login_required
def deleteCoach(request, pk):
    if request.method == 'POST' and request.is_ajax():
        try:
            obj = Coach.objects.get(pk=pk)
            obj.delete()
            return JsonResponse({'status': 'Success', 'messages': 'save successfully'})
        except Coach.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})


@login_required
def coachUpdate(request, pk):
    coach = Coach.objects.get(pk=pk)
    user = User.objects.get(pk=coach.user.pk)
    person = Person.objects.get(pk=coach.person.pk)
    communication = Communication.objects.get(pk=coach.communication.pk)
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

            messages.success(request, 'Antrenör Başarıyla Güncellendi')
            return redirect('wushu:antrenorler')
        else:
            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'antrenor/antrenorDuzenle.html',
                  {'user_form': user_form, 'communication_form': communication_form,
                   'person_form': person_form})
