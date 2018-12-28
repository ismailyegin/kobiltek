from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from oxiterp.serializers import UserSerializer, GroupSerializer
from rest_framework import generics

from patient.forms import PatientForm
from .models import Patient, Threat
from .serializers import PatientSerializer, ThreatSerializer
from datetime import datetime

from django.core import serializers
@login_required
def patients_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients_list.html', {'patients': patients})



@api_view()
@permission_classes((IsAuthenticated, ))
def patients_listJson(request):
    patients = Patient.objects.all()
    data = PatientSerializer(patients, many=True)
    responseData = {}
    responseData['user'] =data.data
    #data = serializers.serialize('json',patients)
    return JsonResponse(responseData, safe=True)


@api_view()
@permission_classes((IsAuthenticated, ))
def getPatient(request, pk):
    patients = Patient.objects.filter(pk=pk)
    data = PatientSerializer(patients, many=True)
    responseData = {}
    responseData['user'] =data.data
    #data = serializers.serialize('json',patients)
    return JsonResponse(responseData, safe=True)


@login_required
def patients_add(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        surname = request.POST.get('surname')
        patientNumber = request.POST.get('patientNumber')
        email = request.POST.get('email')
        mobilePhone = request.POST.get('mobilePhone')
        address = request.POST.get('address')
        birthDate = request.POST.get('birthDate')

        patients = Patient(name=name, surname=surname, patientNumber=patientNumber, email=email, mobilePhone=mobilePhone, address=address, birthDate=birthDate,isActive=True)
        patients.save()

        return redirect('patient:index')

    return render(request, 'patient_add.html')

@login_required
def patiends_add2(request):

    form = PatientForm()

    if request.method == 'POST':

        form = PatientForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('patient:index')
        else:
            return redirect('http://www.oxityazilim.com')

    return render(request, 'patient_add1.html', {'form': form})


@login_required
def patient_update(request, pk):
    patient = get_object_or_404(Patient, pk=pk)

    form = PatientForm(request.POST or None, instance=patient)

    if form.is_valid():
        form.save()
        return redirect('patient:index')

    return render(request, 'patient_add1.html', {'form': form})


@login_required
def patient_delete(request, pk):

    if request.method == 'POST' and request.is_ajax():
        try:
            obj = Patient.objects.get(pk=pk)
            obj.isActive = request.POST['isActive']
            obj.save()
            return JsonResponse({'status': 'Success', 'msg': 'save successfully'})
        except Patient.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})


@api_view()
def getThreatments(request):

    threatmens = Threat.objects.all()
    data = ThreatSerializer(threatmens, many=True)
    responseData = {}
    responseData['threat'] = data.data
    # data = serializers.serialize('json',patients)
    return JsonResponse(responseData, safe=True)