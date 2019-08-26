from django.conf.urls import url

from wushu.Views import DashboardViews, AthleteViews, RefereeViews, ClubViews, CoachViews

app_name = 'wushu'

urlpatterns = [

    # Dashboard
    url(r'anasayfa/admin/$', DashboardViews.return_admin_dashboard, name='admin'),

    # Sporcular
    url(r'sporcu/sporcu-ekle/$', AthleteViews.return_add_athlete, name='sporcu-ekle'),
    url(r'sporcu/sporcular/$', AthleteViews.return_athletes, name='sporcular'),
    url(r'sporcu/kusak/$', AthleteViews.return_belt, name='kusak'),
    url(r'sporcu/kusak/sil/(?P<pk>\d+)$', AthleteViews.categoryItemDelete,
        name='categoryItem-delete'),
    url(r'sporcu/kusakDuzenle/(?P<pk>\d+)$', AthleteViews.categoryItemUpdate,
        name='categoryItem-duzenle'),

    # Hakemler
    url(r'hakem/hakem-ekle/$', RefereeViews.return_add_referee, name='hakem-ekle'),
    url(r'hakem/hakemler/$', RefereeViews.return_referees, name='hakemler'),
    url(r'hakem/seviye/$', RefereeViews.return_level, name='seviye'),
    url(r'hakem/seviye/sil/(?P<pk>\d+)$', RefereeViews.categoryItemDelete,
        name='categoryItem-delete-seviye'),
    url(r'hakem/seviye/(?P<pk>\d+)$', RefereeViews.categoryItemUpdate,
        name='categoryItem-duzenle-seviye'),

    # Kulüler
    url(r'kulup/kulup-ekle/$', ClubViews.return_add_club, name='kulup-ekle'),
    url(r'kulup/kulupler/$', ClubViews.return_clubs, name='kulupler'),

    # Antrenörler
    url(r'antrenor/antrenor-ekle/$', CoachViews.return_add_coach, name='antrenor-ekle'),
    url(r'antrenor/antrenorler/$', CoachViews.return_coachs, name='antrenorler'),
    url(r'antrenor/kademe/$', CoachViews.return_grade, name='kademe'),
    url(r'antrenor/kademe/sil/(?P<pk>\d+)$', CoachViews.categoryItemDelete,
        name='categoryItem-delete-kademe'),
    url(r'antrenor/kademeDuzenle/(?P<pk>\d+)$', CoachViews.categoryItemUpdate,
        name='categoryItem-duzenle-kademe'),

]
