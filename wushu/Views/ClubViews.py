from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def return_add_club(request):
    return render(request, 'kulup/kulup-ekle.html')


@login_required
def return_clubs(request):
    return render(request, 'kulup/kulupler.html')
