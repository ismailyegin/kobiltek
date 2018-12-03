from django.contrib.auth.models import User, Group
from django.shortcuts import render
from rest_framework import viewsets
from oxiterp.serializers import UserSerializer, GroupSerializer
from rest_framework import generics
from .models import Patient
from .serializers import PatientSerializer


def patients_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients_list.html', {'patients': patients})

