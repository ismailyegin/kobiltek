from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def return_admin_dashboard(request):
    return render(request, 'anasayfa/admin.html')


@login_required
def return_athlete_dashboard(request):
    return render(request, 'anasayfa/sporcu.html')


@login_required
def return_referee_dashboard(request):
    return render(request, 'anasayfa/hakem.html')


@login_required
def return_coach_dashboard(request):
    return render(request, 'anasayfa/antrenor.html')


@login_required
def return_directory_dashboard(request):
    return render(request, 'anasayfa/federasyon.html')


@login_required
def return_club_user_dashboard(request):
    return render(request, 'anasayfa/kulup-uyesi.html')
