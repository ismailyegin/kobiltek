from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def return_add_coach(request):
    return render(request, 'antrenor/antrenor-ekle.html')


@login_required
def return_coachs(request):
    return render(request, 'antrenor/antrenorler.html')