from django.conf.urls import url
from django.urls import path
from education.Views import StudentViews, ParentViews, FoodViews, ClassViews, TeacherViews, AttendanceViews

app_name = 'education'

urlpatterns = [
    # path('patients/', ListPatientView.as_view(), name="patients-all"),
    url(r'ogrenci-ekle/$', StudentViews.student_add, name='ogrenci-ekle'),
    url(r'ogrenci-listesi/$', StudentViews.student_list, name='list'),
    url(r'^ogrenci/(?P<pk>\d+)$', StudentViews.getStudent, name='getStudent'),
    url(r'^ogrenci/duzenle/(?P<pk>\d+)$', StudentViews.updateStudent, name='ogrenci-duzenle'),
    url(r'^veli/ekle/(?P<student_pk>\d+)$', ParentViews.parent_add, name='veli-ekle'),
    url(r'^ogrenci-velisi/(?P<pk>\d+)$', ParentViews.getParents, name='getParents'),
    #Yemek URL
    url(r'^yemek-menusu/$', FoodViews.food_list, name='yemek-listesi'),
    url(r'^yemek-menusu/sil/(?P<pk>\d+)$', FoodViews.food_delete, name='yemek-sil'),
    url(r'^yemek-menusu/duzenle/(?P<pk>\d+)$', FoodViews.food_update, name='yemek-duzenle'),

    #Sınıf URL
    url(r'^sinif/$', ClassViews.class_list, name='sinif-listesi'),
    url(r'^sinif/sil/(?P<pk>\d+)$', ClassViews.class_delete, name='sinif-sil'),
    url(r'^sinif/guncelle/(?P<pk>\d+)$', ClassViews.class_update, name='sinif-duzenle'),
    url(r'^sinif/ogrenci-ekle/(?P<pk>\d+)$', ClassViews.class_add_students, name='sinif-ogrenci-ekle'),

    url(r'^sinif-ogrenci-ekle-kaydet/$', ClassViews.student_post, name="sinif-ogrenci-ekle-kaydet"),
    url(r'^sinifin-ogrencileri/(?P<pk>\d+)$', ClassViews.selected_students, name='secilen-ogrenciler'),


    #öğretmen
    url(r'ogretmen/ekle/$', TeacherViews.teacher_add, name='ogretmen-ekle'),
    url(r'ogretmen/liste/$', TeacherViews.teacher_list, name='ogretmen-liste'),
    url(r'^ogretmen/(?P<pk>\d+)$', TeacherViews.getTeacher, name='ogretmen-getir'),
    url(r'^ogretmen/duzenle/(?P<pk>\d+)$', TeacherViews.updateTeacher, name='ogretmen-duzenle'),
    url(r'^ogretmen-aktif-pasif/$', TeacherViews.teacher_active_passive, name="ogretmen-aktif-pasif"),


    #Yoklama
    url(r'yoklama/sinif-liste/$', AttendanceViews.class_list, name='yoklama-sinif-listeleri'),
    #url(r'^yoklama/ogrenci-listesi/(?P<pk>\d+)$', AttendanceViews.student_list, name='yoklama-al'),
    path('yoklama/ogrenci-listesi/<str:class_object>/<str:date>/<str:order>/', AttendanceViews.get_attendance, name='yoklama-al'),
    url(r'^yoklama/gun-yoklamasi/(?P<pk>\d+)$', AttendanceViews.attendances_of_the_day, name='ders-yoklamasi'),
    url(r'^yoklama/yoklama-gonder/$', AttendanceViews.attendance_post, name='yoklama-gonder'),






]
