from django.contrib import admin

from .models import Patient, Threat, CashMovement


class PatientAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'mobilePhone', 'email', 'creationDate', 'totalDebt']
    search_fields = ['name', 'surname']

    class Meta:
        Patient


class ThreatAdmin(admin.ModelAdmin):

    list_display = ['patient', 'threatName', 'price', 'creationDate']

    class Meta:
        Threat


class CashMovementAdmin(admin.ModelAdmin):

    list_display = ['patient', 'price', 'creationDate']


admin.site.register(CashMovement, CashMovementAdmin)

admin.site.register(Patient, PatientAdmin)

admin.site.register(Threat, ThreatAdmin)
