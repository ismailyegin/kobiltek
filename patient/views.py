from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view

from oxiterp.serializers import UserSerializer, GroupSerializer
from rest_framework import generics

from patient.forms import PatientForm
from .models import Patient
from .serializers import PatientSerializer
from datetime import datetime

from django.core import serializers
@login_required
def patients_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients_list.html', {'patients': patients})



@api_view()
def patients_listJson(request):
    patients = Patient.objects.all()
    data = PatientSerializer(patients,many=True)
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

