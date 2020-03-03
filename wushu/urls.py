from django.conf.urls import url

from wushu.Views import DashboardViews, AthleteViews, RefereeViews, ClubViews, CoachViews, DirectoryViews, UserViews, \
    CompetitionViews, AdminViews,HelpViews

app_name = 'wushu'

urlpatterns = [

    # Dashboard
    url(r'anasayfa/admin/$', DashboardViews.return_admin_dashboard, name='admin'),
    url(r'anasayfa/sporcu/$', DashboardViews.return_athlete_dashboard, name='sporcu'),
    url(r'anasayfa/hakem/$', DashboardViews.return_referee_dashboard, name='hakem'),
    url(r'anasayfa/antrenor/$', DashboardViews.return_coach_dashboard, name='antrenor'),
    url(r'anasayfa/federasyon/$', DashboardViews.return_directory_dashboard, name='federasyon'),
    url(r'anasayfa/kulup-uyesi/$', DashboardViews.return_club_user_dashboard, name='kulup-uyesi'),



    # pagenation test
    url(r'sporcu/deneme/$', AthleteViews.deneme, name='deneme'),

    # Sporcular
    url(r'sporcu/sporcu-ekle/$', AthleteViews.return_add_athlete, name='sporcu-ekle'),
    url(r'sporcu/sporcular/$', AthleteViews.return_athletes, name='sporcular'),
    url(r'sporcu/sporcuKusakEkle/(?P<pk>\d+)$', AthleteViews.sporcu_kusak_ekle, name='sporcu-kusak-ekle'),
    url(r'sporcu/sporcuKusakDuzenle/(?P<belt_pk>\d+)/(?P<athlete_pk>\d+)$', AthleteViews.sporcu_kusak_duzenle,
        name='sporcu-kusak-duzenle'),
    url(r'sporcu/sporcuLisansEkle/(?P<pk>\d+)$', AthleteViews.sporcu_lisans_ekle, name='sporcu-lisans-ekle'),
    url(r'sporcu/sporcuLisansDuzenle/(?P<license_pk>\d+)/(?P<athlete_pk>\d+)$', AthleteViews.sporcu_lisans_duzenle,
        name='sporcu-lisans-duzenle'),
    url(r'sporcu/sporcuLisansDuzenle/onayla/(?P<license_pk>\d+)/(?P<athlete_pk>\d+)$',
        AthleteViews.sporcu_lisans_onayla, name='sporcu-lisans-onayla'),

    url(r'sporcu/sporcuLisansDuzenle/reddet/(?P<license_pk>\d+)/(?P<athlete_pk>\d+)$',
        AthleteViews.sporcu_lisans_reddet, name='sporcu-lisans-reddet'),
    url(r'sporcu/sporcuLisansDuzenle/lisanssil/(?P<pk>\d+)/(?P<athlete_pk>\d+)$', AthleteViews.sporcu_lisans_sil,
        name='sporcu-lisans-sil'),
    url(r'sporcu/sporcuLisansListesi/onayla/(?P<license_pk>\d+)$',
        AthleteViews.sporcu_lisans_listesi_onayla, name='sporcu-lisans-listesi-onayla'),
    # lisans listesinin hepsini onaylama
    url(r'sporcu/sporcuLisansListesi/hepsinionayla/$',AthleteViews.sporcu_lisans_listesi_hepsionay, name='sporcu-lisans-hepsini-onayla'),
    # lisanslarin hepsini reddetme
    url(r'sporcu/sporcuLisansListesi/hepsiniReddet/$', AthleteViews.sporcu_lisans_listesi_hepsireddet,
        name='sporcu-lisans-hepsini-reddet'),
    url(r'sporcu/sporcuLisansListesi/reddet/(?P<license_pk>\d+)$',
        AthleteViews.sporcu_lisans_listesi_reddet, name='sporcu-lisans-listesi-reddet'),
    url(r'sporcu/kusak/$', AthleteViews.return_belt, name='kusak'),
    url(r'sporcu/kusak/sil/(?P<pk>\d+)$', AthleteViews.categoryItemDelete,
        name='categoryItem-delete'),
    url(r'sporcu/kusakDuzenle/(?P<pk>\d+)$', AthleteViews.categoryItemUpdate,
        name='categoryItem-duzenle'),
    url(r'sporcu/sporcuKusakDuzenle/onayla/(?P<belt_pk>\d+)/(?P<athlete_pk>\d+)$',
        AthleteViews.sporcu_kusak_onayla, name='sporcu-kusak-onayla'),
    url(r'sporcu/sporcuKusakDuzenle/reddet/(?P<belt_pk>\d+)/(?P<athlete_pk>\d+)$',
        AthleteViews.sporcu_kusak_reddet, name='sporcu-kusak-reddet'),
    url(r'sporcu/sporcuKusakDuzenle/kusaksil/(?P<pk>\d+)/(?P<athlete_pk>\d+)$', AthleteViews.sporcu_kusak_sil,
        name='sporcu-kusak-sil'),
    url(r'sporcu/sporcuKusakListesi/onayla/(?P<belt_pk>\d+)$',
        AthleteViews.sporcu_kusak_listesi_onayla, name='sporcu-kusak-listesi-onayla'),

    url(r'sporcu/sporcuDuzenle/(?P<pk>\d+)$', AthleteViews.updateathletes,
        name='update-athletes'),
    url(r'sporcu/sporcu-kusak-listesi/$', AthleteViews.sporcu_kusak_listesi, name='kusak-listesi'),
    url(r'sporcu/sporcu-lisans-listesi/$', AthleteViews.sporcu_lisans_listesi, name='lisans-listesi'),
    url(r'sporcu/sporcu-profil-guncelle/$', AthleteViews.updateAthleteProfile,
        name='sporcu-profil-guncelle'),

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
    url(r'hakem/hakem-profil-guncelle/$', RefereeViews.updateRefereeProfile,
        name='hakem-profil-guncelle'),

    # Kulüpler
    url(r'kulup/kulup-ekle/$', ClubViews.return_add_club, name='kulup-ekle'),
    url(r'kulup/kulupler/$', ClubViews.return_clubs, name='kulupler'),
    url(r'kulup/kulup-uyesi-ekle/$', ClubViews.return_add_club_person, name='kulup-uyesi-ekle'),
    url(r'kulup/kulup-uyesi-guncelle/(?P<pk>\d+)$', ClubViews.updateClubPersons, name='kulup-uyesi-guncelle'),
    url(r'kulup/kulup-uyeleri/$', ClubViews.return_club_person, name='kulup-uyeleri'),
    url(r'kulup/kulup-uye-rolu/$', ClubViews.return_club_role, name='kulup-uye-rolu'),
    url(r'kulup/kulup-uye-rolu/sil/(?P<pk>\d+)$', ClubViews.deleteClubRole,
        name='ClubRole-delete'),
    url(r'kulup/kulup-uyeleri/sil/(?P<pk>\d+)$', ClubViews.deleteClubUser,
        name='ClubUser-delete'),

    url(r'kulup/kulup-uyeleri/cikar/(?P<pk>\d+)/(?P<club_pk>\d+)/$', ClubViews.deleteClubUserFromClub,
        name='ClubUser-cikar'),
    url(r'kulup/kulup-antrenorleri/cikar/(?P<pk>\d+)/(?P<club_pk>\d+)/$', ClubViews.deleteCoachFromClub,
        name='ClubCoach-cikar'),

    url(r'kulup/kulupRolDuzenle/(?P<pk>\d+)$', ClubViews.updateClubRole,
        name='updateClubRole'),
    url(r'kulup/kulupler/sil/(?P<pk>\d+)$', ClubViews.clubDelete,
        name='delete-club'),
    url(r'kulup/kulupDuzenle/(?P<pk>\d+)$', ClubViews.clubUpdate,
        name='update-club'),
    url(r'kulup/kusak-sinavlari/$', ClubViews.return_belt_exams, name='kusak-sinavlari'),
    url(r'kulup/kusak-sinavi-sporcu-sec/$', ClubViews.choose_athlete, name='kusak-sinavi-sporcu-sec'),
    url(r'kulup/kusak-sinavi-ekle/(?P<athlete1>\S+?)$', ClubViews.add_belt_exam, name='kusak-sinavi-ekle'),
    url(r'kulup/kusak-sinavi-duzenle/$', ClubViews.update_belt_exam, name='kusak-sinavi-duzenle'),
    url(r'kulup/kusak-sinavlari/sil/(?P<pk>\d+)$', ClubViews.delete_belt_exam, name='kusak-sinavi-sil'),
    url(r'kulup/kusak-sinavlari/incele/(?P<pk>\d+)$', ClubViews.detail_belt_exam, name='kusak-sinavi-incele'),
    url(r'kulup/kusak-sinavlari/onayla/(?P<pk>\d+)$', ClubViews.approve_belt_exam, name='kusak-sinavi-onayla'),
    url(r'kulup/kulup-uyesi-profil-guncelle/$', ClubViews.updateClubPersonsProfile,
        name='kulup-uyesi-profil-guncelle'),

    url(r'kulup/kulup-uyesi-sec/(?P<pk>\d+)$', ClubViews.choose_sport_club_user,
        name='choose-sport-club-user'),

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
    url(r'antrenor/antrenorSec/(?P<pk>\d+)$', ClubViews.choose_coach,
        name='choose-coach'),
    url(r'antrenor/antrenor-profil-guncelle/$', CoachViews.updateCoachProfile,
        name='antrenor-profil-guncelle'),
    url(r'antrenor/antrenorkademeekle/(?P<pk>\d+)$', CoachViews.antrenor_kademe_ekle, name='antrenor-kademe-ekle'),

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
    url(r'yonetim/kurul-uye-rol-duzenle/(?P<pk>\d+)$', DirectoryViews.update_member_role,
        name='kurul-uye-rol-duzenle'),
    url(r'yonetim/kurullar/$', DirectoryViews.return_commissions, name='kurullar'),
    url(r'yonetim/kurullar/sil/(?P<pk>\d+)$', DirectoryViews.delete_commission,
        name='kurul_sil'),
    url(r'yonetim/kurul-duzenle/(?P<pk>\d+)$', DirectoryViews.update_commission,
        name='kurul-duzenle'),
    url(r'yonetim/yonetim-kurul-profil-guncelle/$', DirectoryViews.updateDirectoryProfile,
        name='yonetim-kurul-profil-guncelle'),

    # Admin
    url(r'admin/admin-profil-guncelle/$', AdminViews.updateProfile,
        name='admin-profil-guncelle'),

    # Kullanıcılar
    url(r'kullanici/kullanicilar/$', UserViews.return_users, name='kullanicilar'),
    url(r'kullanici/kullanici-duzenle/(?P<pk>\d+)$', UserViews.update_user, name='kullanici-duzenle'),
    url(r'kullanici/kullanicilar/aktifet/(?P<pk>\d+)$', UserViews.active_user,
        name='kullanici-aktifet'),
    url(r'kullanici/kullanicilar/kullanici-bilgi-gonder/(?P<pk>\d+)$', UserViews.send_information,
        name='kullanici-bilgi-gonder'),

    #Competition
    url(r'musabaka/musabakalar/$', CompetitionViews.return_competitions, name='musabakalar'),
    url(r'musabaka/musabaka-ekle/$', CompetitionViews.musabaka_ekle, name='musabaka-ekle'),
    url(r'musabaka/musabaka-duzenle/(?P<pk>\d+)$', CompetitionViews.musabaka_duzenle, name='musabaka-duzenle'),
    url(r'musabaka/musabakalar/musabaka-sil(?P<pk>\d+)$', CompetitionViews.musabaka_sil, name='musabaka-sil'),
    url(r'musabaka/musabaka-duzenle/musabaka-sporcu-sec(?P<pk>\d+)$', CompetitionViews.musabaka_sporcu_sec,
        name='musabaka-sporcu-sec'),
    url(r'musabaka/musabaka-duzenle/kaldir/(?P<pk>\d+)/$', CompetitionViews.musabaka_sporcu_sil,
        name='musabaka-sporcu-kaldir'),
#     Yardım ve destek

    url(r'yardim$', HelpViews.help, name='help'),

]
