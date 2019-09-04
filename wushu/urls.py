from django.conf.urls import url

from wushu.Views import DashboardViews, AthleteViews, RefereeViews, ClubViews, CoachViews, DirectoryViews

app_name = 'wushu'

urlpatterns = [

    # Dashboard
    url(r'anasayfa/admin/$', DashboardViews.return_admin_dashboard, name='admin'),

    # Sporcular
    url(r'sporcu/sporcu-ekle/$', AthleteViews.return_add_athlete, name='sporcu-ekle'),
    url(r'sporcu/sporcular/$', AthleteViews.return_athletes, name='sporcular'),
    url(r'sporcu/sporcuKusakEkle/(?P<pk>\d+)$', AthleteViews.sporcu_kusak_ekle, name='sporcu-kusak-ekle'),
    url(r'sporcu/sporcuKusakDuzenle/(?P<belt_pk>\d+)/(?P<athlete_pk>\d+)$', AthleteViews.sporcu_kusak_duzenle,
        name='sporcu-kusak-duzenle'),
    url(r'sporcu/sporcuLisansEkle/(?P<pk>\d+)$', AthleteViews.sporcu_lisans_ekle, name='sporcu-lisans-ekle'),
    url(r'sporcu/sporcuLisansDuzenle/(?P<license_pk>\d+)/(?P<athlete_pk>\d+)$', AthleteViews.sporcu_lisans_duzenle,
        name='sporcu-lisans-duzenle'),
    url(r'sporcu/kusak/$', AthleteViews.return_belt, name='kusak'),
    url(r'sporcu/kusak/sil/(?P<pk>\d+)$', AthleteViews.categoryItemDelete,
        name='categoryItem-delete'),
    url(r'sporcu/kusakDuzenle/(?P<pk>\d+)$', AthleteViews.categoryItemUpdate,
        name='categoryItem-duzenle'),
    url(r'sporcu/sporcuDuzenle/(?P<pk>\d+)$', AthleteViews.updateathletes,
        name='update-athletes'),

    # Hakemler
    url(r'hakem/hakem-ekle/$', RefereeViews.return_add_referee, name='hakem-ekle'),
    url(r'hakem/hakemler/$', RefereeViews.return_referees, name='hakemler'),
    url(r'hakem/seviye/$', RefereeViews.return_level, name='seviye'),
    url(r'hakem/seviye/sil/(?P<pk>\d+)$', RefereeViews.categoryItemDelete,
        name='categoryItem-delete-seviye'),
    url(r'hakem/seviye/(?P<pk>\d+)$', RefereeViews.categoryItemUpdate,
        name='categoryItem-duzenle-seviye'),
    url(r'hakem/hakemler/sil/(?P<pk>\d+)$', RefereeViews.deleteReferee,
        name='referee-delete'),
    url(r'hakem/hakemDuzenle/(?P<pk>\d+)$', RefereeViews.updateReferee,
        name='hakem-duzenle'),

    # Kulüler
    url(r'kulup/kulup-ekle/$', ClubViews.return_add_club, name='kulup-ekle'),
    url(r'kulup/kulupler/$', ClubViews.return_clubs, name='kulupler'),
    url(r'kulup/kulup-uyesi-ekle/(?P<pk>\d+)$', ClubViews.return_add_club_person, name='kulup-uyesi-ekle'),
    url(r'kulup/kulup-uyesi-guncelle/(?P<pk>\d+)$', ClubViews.updateClubPersons, name='kulup-uyesi-guncelle'),
    url(r'kulup/kulup-uyeleri/$', ClubViews.return_club_person, name='kulup-uyeleri'),
    url(r'kulup/kulup-uye-rolu/$', ClubViews.return_club_role, name='kulup-uye-rolu'),
    url(r'kulup/kulup-uye-rolu/sil/(?P<pk>\d+)$', ClubViews.deleteClubRole,
        name='ClubRole-delete'),
    url(r'kulup/kulupRolDuzenle/(?P<pk>\d+)$', ClubViews.updateClubRole,
        name='updateClubRole'),
    url(r'kulup/kulupler/sil/(?P<pk>\d+)$', ClubViews.clubDelete,
        name='delete-club'),
    url(r'kulup/kulupDuzenle/(?P<pk>\d+)$', ClubViews.clubUpdate,
        name='update-club'),

    # Antrenörler
    url(r'antrenor/antrenor-ekle/$', CoachViews.return_add_coach, name='antrenor-ekle'),
    url(r'antrenor/antrenorler/$', CoachViews.return_coachs, name='antrenorler'),
    url(r'antrenor/kademe/$', CoachViews.return_grade, name='kademe'),
    url(r'antrenor/kademe/sil/(?P<pk>\d+)$', CoachViews.categoryItemDelete,
        name='categoryItem-delete-kademe'),
    url(r'antrenor/kademeDuzenle/(?P<pk>\d+)$', CoachViews.categoryItemUpdate,
        name='categoryItem-duzenle-kademe'),
    url(r'antrenor/antrenorler/sil/(?P<pk>\d+)$', CoachViews.deleteCoach,
        name='delete-coach'),
    url(r'antrenor/antrenorDuzenle/(?P<pk>\d+)$', CoachViews.coachUpdate,
        name='update-coach'),

    # Yönetim Kurulu
    url(r'yonetim/kurul-uyeleri/$', DirectoryViews.return_directory_members, name='kurul-uyeleri'),
    url(r'yonetim/kurul-uyesi-ekle/$', DirectoryViews.add_directory_member, name='kurul-uyesi-ekle'),
    url(r'yonetim/kurul-uyesi-duzenle/(?P<pk>\d+)$', DirectoryViews.update_directory_member,
        name='kurul-uyesi-duzenle'),
    url(r'yonetim/kurul-uyeleri/sil/(?P<pk>\d+)$', DirectoryViews.delete_directory_member,
        name='kurul-uyesi-sil'),
    url(r'yonetim/kurul-uye-rolleri/$', DirectoryViews.return_member_roles, name='kurul-uye-rolleri'),
    url(r'yonetim/kurul-uye-rolleri/sil/(?P<pk>\d+)$', DirectoryViews.delete_member_role,
        name='kurul_uye_rol_sil'),
    url(r'yonetim/kurul_uye_rol_duzenle/(?P<pk>\d+)$', DirectoryViews.update_member_role,
        name='kurul_uye_rol_duzenle'),
    url(r'yonetim/kurullar/$', DirectoryViews.return_commissions, name='kurullar'),
    url(r'yonetim/kurullar/sil/(?P<pk>\d+)$', DirectoryViews.delete_commission,
        name='kurul_sil'),
    url(r'yonetim/kurul_duzenle/(?P<pk>\d+)$', DirectoryViews.update_commission,
        name='kurul_duzenle'),

]
