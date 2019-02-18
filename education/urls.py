from django.conf.urls import url
from django.urls import path
from education.Views import StudentViews


app_name = 'education'

urlpatterns = [
    # path('patients/', ListPatientView.as_view(), name="patients-all"),
    url(r'^$', StudentViews.student_add, name='index'),
    url(r'ogrenci-listesi/$', StudentViews.student_list, name='list'),
    url(r'^ogrenci/(?P<pk>\d+)$', StudentViews.getStudent, name='getStudent'),
    url(r'^ogrenci/duzenle/(?P<pk>\d+)$', StudentViews.updateStudent, name='ogrenci-duzenle'),


]
