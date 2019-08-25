from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from wushu.Forms.ClubForm import ClubForm
from wushu.Forms.CommunicationForm import CommunicationForm
from wushu.models import SportsClub


@login_required
def return_add_club(request):
    club_form = ClubForm()
    communication_form = CommunicationForm()

    if request.method == 'POST':

        club_form = ClubForm(request.POST, request.FILES)
        communication_form = CommunicationForm(request.POST, request.FILES)

        if club_form.is_valid() and communication_form.is_valid():
            club = club_form.save(commit=False)
            communication = communication_form.save(commit=False)
            communication.save()
            club.save()

            clubsave = SportsClub(communication=communication,
                                  name=club_form.cleaned_data['name'],
                                  shortName=club_form.cleaned_data['shortName'],
                                  foundingDate=club_form.cleaned_data['foundingDate'],
                                  logo=club_form.cleaned_data['logo'],
                                  clubMail=club_form.cleaned_data['clubMail']

                                  )

            clubsave.save()

            messages.success(request, 'Kulüp Başarıyla Kayıt Edilmiştir.')

            return redirect('wushu:kulup-ekle')

        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'kulup/kulup-ekle.html',
                  {'club_form': club_form, 'communication_form': communication_form})


@login_required
def return_clubs(request):
    return render(request, 'kulup/kulupler.html')
