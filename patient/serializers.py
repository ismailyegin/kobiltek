from rest_framework import serializers
from .models import Patient, Threat


class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = '__all__'


class ThreatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Threat
        fields = '__all__'