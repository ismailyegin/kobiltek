from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from rest_framework import viewsets
from oxiterp.serializers import UserSerializer, GroupSerializer
from rest_framework import generics
from .models import Patient
from .serializers import PatientSerializer
from datetime import datetime
@login_required
def patients_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients_list.html', {'patients': patients})

@login_required
def patients_add(request):

    if request.method == 'POST':

        name= request.POST.get('name')
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


