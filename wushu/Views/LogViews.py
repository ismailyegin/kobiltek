from builtins import print, set, property, int
from datetime import timedelta, datetime
from operator import attrgetter
from os import name

from django.db.models.functions import Lower

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect

from wushu.services import general_methods
from wushu.Forms.UserSearchForm import UserSearchForm
from wushu.models.Logs import Logs

from wushu.models.Athlete import Athlete


@login_required
def return_log(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    logs = Logs.objects.none()
    user_form = UserSearchForm()
    if request.method == 'POST':
        user_form = UserSearchForm(request.POST)
        if user_form.is_valid():
            firstName = user_form.cleaned_data.get('first_name')
            lastName = user_form.cleaned_data.get('last_name')
            email = user_form.cleaned_data.get('email')
            playDate = request.POST.get('playDate')
            finishDate = request.POST.get('finishDate')
            if playDate:
                playDate = datetime.strptime(playDate, '%d/%m/%Y').date()

            if finishDate:
                finishDate = datetime.strptime(finishDate, "%d/%m/%Y").date()

            if not (firstName or lastName or email or playDate or finishDate):
                logs = Logs.objects.all().order_by('-creationDate')

            else:
                query = Q()
                if lastName:
                    query &= Q(user__last_name__icontains=lastName)
                if firstName:
                    query &= Q(user__first_name__icontains=firstName)
                if email:
                    query &= Q(user__email__icontains=email)
                if playDate:
                    query &= Q(creationDate__gte=playDate)
                if finishDate:
                    query &= Q(creationDate__lt=finishDate)

                logs = Logs.objects.filter(query).order_by('-creationDate')
    return render(request, 'Log/Logs.html', {'logs': logs, 'user_form': user_form})


@login_required
def control(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    athletes = Athlete.objects.none()
    for athlete in Athlete.objects.all():
        if athlete.belts.filter(isActive=True).count() > 1:
            athletes |= athlete

    return render(request, 'sporcu/sporcular.html', {'athletes': athletes, })
