from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse


from wushu.Forms.CompetitionForm import CompetitionForm
from wushu.models import SportClubUser, SportsClub, Competition, Athlete
from wushu.models.EnumFields import EnumFields
from wushu.models.SandaAthlete import SandaAthlete

from wushu.models.TaoluCategori import TaoluCategori
from wushu.models.CompetitionCategori import CompetitionCategori



from wushu.services import general_methods


@login_required
def return_competitions(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')

    competitions = Competition.objects.all()

    return render(request, 'musabaka/musabakalar.html', {'competitions': competitions})


@login_required
def musabaka_ekle(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    competition_form = CompetitionForm()
    if request.method == 'POST':
        competition_form = CompetitionForm(request.POST)
        if competition_form.is_valid():
            competition_form.save()
            messages.success(request, 'Müsabaka Başarıyla Kaydedilmiştir.')

            return redirect('wushu:musabakalar')
        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'musabaka/musabaka-ekle.html',
                  {'competition_form': competition_form})


@login_required
def musabaka_duzenle(request, pk):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')

    musabaka = Competition.objects.get(pk=pk)
    categori = musabaka.categori.none()
    athletes = SandaAthlete.objects.none()
    if musabaka.subBranch == EnumFields.SANDA:
        athletes = SandaAthlete.objects.filter(competition=musabaka.pk)
    if musabaka.subBranch == 'TAOLU':
        categori = musabaka.categori.all()

    competition_form = CompetitionForm(request.POST or None, instance=musabaka)
    if request.method == 'POST':
        if competition_form.is_valid():
            competition_form.save()
            messages.success(request, 'Müsabaka Başarıyla Güncellenmiştir.')

            return redirect('wushu:musabaka-duzenle', pk=pk)
        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'musabaka/musabaka-duzenle.html',
                  {'competition_form': competition_form, 'competition': musabaka, 'athletes': athletes,
                   'categori': categori})


@login_required
def musabaka_sil(request, pk):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    if request.method == 'POST' and request.is_ajax():
        try:
            obj = Competition.objects.get(pk=pk)
            obj.delete()
            return JsonResponse({'status': 'Success', 'messages': 'save successfully'})
        except Competition.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})


@login_required
def musabaka_sporcu_sec(request, pk):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    login_user = request.user
    user = User.objects.get(pk=login_user.pk)
    competition = Competition.objects.get(pk=pk)
    if user.groups.filter(name='KulupUye'):
        sc_user = SportClubUser.objects.get(user=user)
        clubsPk = []
        clubs = SportsClub.objects.filter(clubUser=sc_user)
        for club in clubs:
            clubsPk.append(club.pk)
        athletes = Athlete.objects.filter(licenses__sportsClub__in=clubsPk).distinct()
    elif user.groups.filter(name__in=['Yonetim', 'Admin']):
        athletes = Athlete.objects.all()
    if request.method == 'POST':

        athletes1 = request.POST.getlist('selected_options')
        if athletes1:
            for x in athletes1:
                if competition.subBranch == 'SANDA':
                    athlete = Athlete.objects.get(pk=x)
                    sandaAthlete = SandaAthlete()
                    sandaAthlete.athlete = athlete
                    sandaAthlete.competition = competition
                    sandaAthlete.save()

        return redirect('wushu:musabaka-duzenle', pk=pk)
    return render(request, 'kulup/kusak-sinavi-sporcu-sec.html', {'athletes': athletes})


@login_required
def musabaka_sporcu_sil(request, pk):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    if request.method == 'POST' and request.is_ajax():
        try:
            athlete = SandaAthlete.objects.get(pk=pk)
            athlete.delete()
            return JsonResponse({'status': 'Success', 'messages': 'save successfully'})
        except SandaAthlete.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})


@login_required
def musabaka_kategori_sec(request, pk):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    login_user = request.user
    user = User.objects.get(pk=login_user.pk)
    competition = Competition.objects.get(pk=pk)
    kategoriler = competition.categori.all()
    coa = []
    for item in kategoriler:
        coa.append(item.pk)
    categori = TaoluCategori.objects.exclude(competitioncategori__in=coa)
    if request.method == 'POST':
        kategoriler = request.POST.getlist('selected_options')
        if kategoriler:
            for x in kategoriler:
                if competition.subBranch == 'TAOLU':
                    kategori = TaoluCategori.objects.get(pk=x)
                    competitionCategori = CompetitionCategori()
                    competitionCategori.categori = kategori
                    competitionCategori.save()
                    competition.categori.add(competitionCategori)
                    competition.save()

        return redirect('wushu:musabaka-duzenle', pk=pk)
    return render(request, 'musabaka/musabaka-Kategori-sec.html', {'categori': categori})


@login_required
def musabaka_categori_sil(request, pk, competition):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    if request.method == 'POST' and request.is_ajax():
        try:
            musabaka = Competition.objects.get(pk=competition)
            kategori = CompetitionCategori.objects.get(pk=pk)
            kategori.delete()

            return JsonResponse({'status': 'Success', 'messages': 'save successfully'})
        except SandaAthlete.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})


@login_required
def return_sporcu(request):
    login_user = request.user
    user = User.objects.get(pk=login_user.pk)

    kategori = CompetitionCategori.objects.none()
    # print("ajax istenilen yere geldi")

    # /datatablesten gelen veri kümesi datatables degiskenine alindi
    if request.method == 'GET':
        datatables = request.GET
        kategori = CompetitionCategori.objects.get(pk=request.GET.get('cmd'))

    elif request.method == 'POST':
        datatables = request.POST
        # print(datatables)
        # print("post islemi gerceklesti")

    # /Sayfanın baska bir yerden istenmesi durumunda degerlerin None dönmemesi icin degerler try boklari icerisine alindi
    try:
        draw = int(datatables.get('draw'))
        # print("draw degeri =", draw)
        # Ambil start
        start = int(datatables.get('start'))
        # print("start degeri =", start)
        # Ambil length (limit)
        length = int(datatables.get('length'))
        # print("lenght  degeri =", length)
        # Ambil data search
        search = datatables.get('search[value]')
        # print("search degeri =", search)
    except:
        draw = 1
        start = 0
        length = 10

    if length == -1:
        if user.groups.filter(name='KulupUye'):
            sc_user = SportClubUser.objects.get(user=user)
            clubsPk = []
            clubs = SportsClub.objects.filter(clubUser=sc_user)
            for club in clubs:
                clubsPk.append(club.pk)

            modeldata = kategori.athlete.filter(licenses__sportsClub__in=clubsPk).distinct()
            total = modeldata.count()

        elif user.groups.filter(name__in=['Yonetim', 'Admin']):
            modeldata = kategori.athlete.all()
            total = kategori.athlete.all().count()


    else:
        if search:
            modeldata = kategori.athlete.filter(
                Q(user__last_name__icontains=search) | Q(user__first_name__icontains=search) | Q(
                    user__email__icontains=search))
            total = modeldata.count();

        else:
            if user.groups.filter(name='KulupUye'):
                sc_user = SportClubUser.objects.get(user=user)
                clubsPk = []
                clubs = SportsClub.objects.filter(clubUser=sc_user)
                for club in clubs:
                    clubsPk.append(club.pk)
                modeldata = kategori.athlete.filter(licenses__sportsClub__in=clubsPk).distinct()[start:start + length]
                total = kategori.athlete.all().count()
            elif user.groups.filter(name__in=['Yonetim', 'Admin']):

                modeldata = kategori.athlete.all()[start:start + length]
                total = kategori.athlete.all().count()

    say = start + 1
    start = start + length
    page = start / length

    beka = []
    for item in modeldata:
        data = {
            'say': say,
            'pk': item.pk,
            'name': item.user.first_name + item.user.last_name,
            # 'user': item.person.birthDate,
            #             # 'klup': klup,
            #             # 'brans': brans,
            #             # 'kusak': kusak,

        }
        beka.append(data)
        say += 1

    response = {

        'data': beka,
        'draw': draw,
        'recordsTotal': total,
        'recordsFiltered': total,

    }
    return JsonResponse(response)


# sporcu seç
@login_required
def choose_athlete(request, pk, competition):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    login_user = request.user
    user = User.objects.get(pk=login_user.pk)
    kategori = CompetitionCategori.objects.get(pk=pk)
    athletes = Athlete.objects.none()

    if request.method == 'POST':

        athletes1 = request.POST.getlist('selected_options')
        if athletes1:
            for x in athletes1:
                kategori.athlete.add(x)
                kategori.save()
        return redirect('wushu:musabaka-duzenle', pk=competition)
    return render(request, 'musabaka/musabaka-Sporcu-sec.html',
                  {'athletes': athletes, 'kategori': kategori, 'competition': competition})


@login_required
def return_sporcu_sec(request):
    login_user = request.user
    user = User.objects.get(pk=login_user.pk)

    kategori = CompetitionCategori.objects.none()

    # /datatablesten gelen veri kümesi datatables degiskenine alindi
    if request.method == 'GET':
        datatables = request.GET
        kategori = CompetitionCategori.objects.get(pk=request.GET.get('kategori'))


    elif request.method == 'POST':
        datatables = request.POST
        # print(datatables)
        # print("post islemi gerceklesti")

    # /Sayfanın baska bir yerden istenmesi durumunda degerlerin None dönmemesi icin degerler try boklari icerisine alindi
    try:
        draw = int(datatables.get('draw'))
        # print("draw degeri =", draw)
        # Ambil start
        start = int(datatables.get('start'))
        # print("start degeri =", start)
        # Ambil length (limit)
        length = int(datatables.get('length'))
        # print("lenght  degeri =", length)
        # Ambil data search
        search = datatables.get('search[value]')
        # print("search degeri =", search)
    except:
        draw = 1
        start = 0
        length = 10

    if length == -1:
        if user.groups.filter(name='KulupUye'):
            sc_user = SportClubUser.objects.get(user=user)
            clubsPk = []
            clubs = SportsClub.objects.filter(clubUser=sc_user)
            for club in clubs:
                clubsPk.append(club.pk)
            coa = []
            for item in kategori.athlete.all():
                coa.append(item.user.pk)

            modeldata = Athlete.objects.filter(licenses__sportsClub__in=clubsPk).exclude(
                competitioncategori__athlete__user_id__in=coa)
            total = modeldata.count()
            # .exclude(belts=None).exclude(licenses=None).exclude(beltexam__athletes__user__in = exam_athlete).filter(licenses__branch=sinav.branch,licenses__status='Onaylandı').filter(belts__branch=sinav.branch,belts__status='Onaylandı').distinct()
        elif user.groups.filter(name__in=['Yonetim', 'Admin']):
            coa = []
            for item in kategori.athlete.all():
                coa.append(item.user.pk)
            modeldata = Athlete.objects.exclude(user__in=coa)
            total = modeldata.count()

            # print('elimizde olanlar', athletes)
            # kategori.athlete.exclude(
            # exclude(belts=None).exclude(licenses=None).exclude(beltexam__athletes__user__in = exam_athlete).filter(licenses__branch=sinav.branch,licenses__status='Onaylandı').filter(belts__branch=sinav.branch,belts__status='Onaylandı')
        #   .exclude(belts__definition__parent_id=None)    eklenmeli ama eklendigi zaman kuşaklarindan bir tanesi en üst olunca almıyor




    else:
        if search:

            if user.groups.filter(name='KulupUye'):
                sc_user = SportClubUser.objects.get(user=user)
                clubsPk = []
                clubs = SportsClub.objects.filter(clubUser=sc_user)
                for club in clubs:
                    clubsPk.append(club.pk)
                coa = []
                for item in kategori.athlete.all():
                    coa.append(item.user.pk)

                modeldata = Athlete.objects.filter(licenses__sportsClub__in=clubsPk).exclude(
                    competitioncategori__athlete__user_id__in=coa).filter(
                Q(user__last_name__icontains=search) | Q(user__first_name__icontains=search) | Q(
                    user__email__icontains=search))
                total = modeldata.count()
                # .exclude(belts=None).exclude(licenses=None).exclude(beltexam__athletes__user__in = exam_athlete).filter(licenses__branch=sinav.branch,licenses__status='Onaylandı').filter(belts__branch=sinav.branch,belts__status='Onaylandı').distinct()
            elif user.groups.filter(name__in=['Yonetim', 'Admin']):
                coa = []
                for item in kategori.athlete.all():
                    coa.append(item.user.pk)
                modeldata = Athlete.objects.exclude(user__in=coa).filter(
                    Q(user__last_name__icontains=search) | Q(user__first_name__icontains=search) | Q(
                        user__email__icontains=search))
                total = modeldata.count()

        else:
            if user.groups.filter(name='KulupUye'):
                sc_user = SportClubUser.objects.get(user=user)
                clubsPk = []
                clubs = SportsClub.objects.filter(clubUser=sc_user)
                for club in clubs:
                    clubsPk.append(club.pk)
                coa = []
                for item in kategori.athlete.all():
                    coa.append(item.user.pk)

                modeldata = Athlete.objects.filter(licenses__sportsClub__in=clubsPk).exclude(
                    competitioncategori__athlete__user_id__in=coa)[start:start + length]
                # .exclude(belts=None).exclude(licenses=None).exclude(beltexam__athletes__user__in = exam_athlete).filter(licenses__branch=sinav.branch,licenses__status='Onaylandı').filter(belts__branch=sinav.branch,belts__status='Onaylandı').distinct()
            elif user.groups.filter(name__in=['Yonetim', 'Admin']):
                coa = []
                for item in kategori.athlete.all():
                    coa.append(item.user.pk)
                modeldata = Athlete.objects.exclude(user__in=coa)[start:start + length]
                total = Athlete.objects.exclude(user__in=coa).count()

    say = start + 1
    start = start + length
    page = start / length

    beka = []
    for item in modeldata:
        data = {
            'say': say,
            'pk': item.pk,
            'name': item.user.first_name + item.user.last_name,

        }
        beka.append(data)
        say += 1

    response = {

        'data': beka,
        'draw': draw,
        'recordsTotal': total,
        'recordsFiltered': total,

    }
    return JsonResponse(response)
