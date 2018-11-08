from django.urls import path
from .views import ListPatientView


urlpatterns = [
    path('patients/', ListPatientView.as_view(), name="patients-all")
]