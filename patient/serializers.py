from django.contrib.auth.models import Permission
from rest_framework import serializers
from .models import Patient, Threat


class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = ('name', 'surname', 'email', 'mobilePhone', 'address',  'patientNumber', 'creationDate','birthDate', 'creationDate', 'isActive', 'totalDebt')


class ThreatSerializer(serializers.ModelSerializer):



    class Meta:
        model = Threat
        fields = ('threatName','price','patient')
        depth = 2


class PermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Permission
        fields = '__all__'