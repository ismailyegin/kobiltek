from django.conf.urls import url
from django.urls import path
from .import views


app_name = 'patient'

urlpatterns = [
    # path('patients/', ListPatientView.as_view(), name="patients-all"),
    url(r'^$', views.patients_list, name='index'),

    url(r'^hasta/ekle/$', views.patients_add, name='hasta-ekle')

]
