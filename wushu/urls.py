from django.conf.urls import url

from wushu.Views import DashboardViews, AthleteViews, RefereeViews, ClubViews, CoachViews, BranchViews

app_name = 'wushu'

urlpatterns = [

    # Dashboard
    url(r'anasayfa/admin/$', DashboardViews.return_admin_dashboard, name='admin'),

    # Sporcular
    url(r'sporcu/sporcu-ekle/$', AthleteViews.return_add_athlete, name='sporcu-ekle'),
    url(r'sporcu/sporcular/$', AthleteViews.return_athletes, name='sporcular'),

    # Hakemler
    url(r'hakem/hakem-ekle/$', RefereeViews.return_add_referee, name='hakem-ekle'),
    url(r'hakem/hakemler/$', RefereeViews.return_referees, name='hakemler'),

    # Kulüler
    url(r'kulup/kulup-ekle/$', ClubViews.return_add_club, name='kulup-ekle'),
    url(r'kulup/kulupler/$', ClubViews.return_clubs, name='kulupler'),

    # Antrenörler
    url(r'antrenor/antrenor-ekle/$', CoachViews.return_add_coach, name='antrenor-ekle'),
    url(r'antrenor/antrenorler/$', CoachViews.return_coachs, name='antrenorler'),

    # Branşlar
    url(r'brans/brans-ekle/$', BranchViews.return_add_branch, name='brans-ekle'),
    url(r'brans/branslar/$', BranchViews.return_branchs, name='branslar'),
]
