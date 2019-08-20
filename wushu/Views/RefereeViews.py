from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def return_add_referee(request):
    return render(request, 'hakem/hakem-ekle.html')


@login_required
def return_referees(request):
    return render(request, 'hakem/hakemler.html')