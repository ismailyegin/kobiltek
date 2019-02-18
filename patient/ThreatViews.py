from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view

from patient.forms import ThreatForm
from patient.models import Threat
from patient.serializers import PermissionSerializer


@login_required
def threats_list(request):
    threats= Threat.objects.all()
    return render(request, 'threat_list.html', {'threats': threats})



@login_required
def threat_add(request):

    form = ThreatForm()

    if request.method == 'POST':

        form = ThreatForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('patient:muayene')
        else:
            return redirect('http://www.oxityazilim.com')

    return render(request, 'threat_add.html', {'form': form})




@login_required
@permission_required('threat.change_threat', login_url='/accounts/login')
def threat_update(request, pk):
    threat = get_object_or_404(Threat, pk=pk)

    form = ThreatForm(request.POST or None, instance=threat)

    if form.is_valid():
        form.save()
        return redirect('patient:muayene')

    return render(request, 'threat_add.html', {'form': form})


@api_view()
def getPermission(request):
    patients = Permission.objects.all()
    data = PermissionSerializer(patients, many=True)
    responseData = {}
    responseData['user'] = data.data
    # data = serializers.serialize('json',patients)
    return JsonResponse(responseData, safe=True)