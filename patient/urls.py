from django.conf.urls import url
from django.urls import path
from .import views

urlpatterns = [
    # path('patients/', ListPatientView.as_view(), name="patients-all"),
    url(r'^$', views.patients_list)

]
