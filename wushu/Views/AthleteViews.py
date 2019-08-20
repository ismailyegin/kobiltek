from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def return_add_athlete(request):
    return render(request, 'sporcu/sporcu-ekle.html')


@login_required
def return_athletes(request):
    return render(request, 'sporcu/sporcular.html')
