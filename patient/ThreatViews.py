from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from patient.forms import ThreatForm
from patient.models import Threat


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