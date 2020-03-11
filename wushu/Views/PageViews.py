from datetime import timedelta, datetime

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect

from wushu.Forms.BeltForm import BeltForm
from wushu.Forms.CategoryItemForm import CategoryItemForm
from wushu.Forms.CommunicationForm import CommunicationForm
from wushu.Forms.DisabledCommunicationForm import DisabledCommunicationForm
from wushu.Forms.DisabledPersonForm import DisabledPersonForm
from wushu.Forms.DisabledUserForm import DisabledUserForm
from wushu.Forms.LicenseForm import LicenseForm
from wushu.Forms.UserForm import UserForm
from wushu.Forms.PersonForm import PersonForm
from wushu.Forms.UserSearchForm import UserSearchForm
from wushu.models import Athlete, CategoryItem, Person, Communication, License, SportClubUser, SportsClub
from wushu.models.EnumFields import EnumFields
from wushu.models.Level import Level
from wushu.services import general_methods

# page
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def deneme(request):
    return render(request, 'sporcu/deneme.html')


@login_required
def return_athletesdeneme(request):
    # print("ajax istenilen yere geldi")

    # /datatablesten gelen veri kümesi datatables degiskenine alindi
    if request.method == 'GET':
        datatables = request.GET
        # print("get islemi gerceklesti")
    elif request.method == 'POST':
        datatables = request.POST
        # print("post islemi gerceklesti")

    print(datatables)
    # /Sayfanın baska bir yerden istenmesi durumunda degerlerin None dönmemesi icin degerler try boklari icerisine alindi
    try:
        draw = int(datatables.get('draw'))
        print("draw degeri =", draw)
        # Ambil start
        start = int(datatables.get('start'))
        print("start degeri =", start)
        # Ambil length (limit)
        length = int(datatables.get('length'))
        print("lenght  degeri =", length)
        # Ambil data search
        search = datatables.get('search[value]')
        print("search degeri =", search)
    except:
        draw = 1
        start = 0
        length = 10

    # object_list = MyModel.objects.all()

    # Test verisi elde edebilemek icin sisteme kayıt saglandi

    # for x in range(150):
    #     b = MyModel(name='İsmail Yegin', user='Admin.', value='Kobiltek')
    #     b.save()

    if search:
        modeldata = Athlete.objects.filter(
            Q(user__last_name__icontains=search) | Q(user__first_name__icontains=search) | Q(
                user__email__icontains=search))
        total = modeldata.count();
        print("gelen deger=", total)
        # length=1000
        # llll=0
        # page=1

    else:
        modeldata = Athlete.objects.all()

        total = Athlete.objects.count()

    if length == -1:
        print("deger bekledigimiz gibi geldi")

    # /Sayfalama  islemleri ile gerekli bir sekil de istenilen sayfanın gönderilmesi gerçeklesitirildi.

    start = start + length
    page = start / length

    beka = []
    say = 1

    for item in modeldata:


        data = {
            'say': say,
            'pk': item.pk,
            'name': item.user.first_name + item.user.last_name,
            'user': item.person.birthDate,
            'klup': '-',
            'brans': '-',
            'kusak': '-',

        }
        beka.append(data)
        say += 1

    # veri = [item.to_dict_json(say)  for item in modeldata ]

    paginator = Paginator(beka, length)
    # print("paginator=", paginator)
    veri = paginator.page(page).object_list
    # print("veri=", veri)

    # Veri istenildigi gibi paketlendi ve gönderildi
    response = {

        'data': veri,
        'draw': draw,
        'recordsTotal': total,
        'recordsFiltered': total,
        'start': start

    }
    # print("response degeri =", response)
    return JsonResponse(response)




