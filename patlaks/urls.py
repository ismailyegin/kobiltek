from django.conf.urls import url, include
from django.urls import path

from patlaks.Views import CompetitorViews, FakeViews, CompetitorApiViews2

app_name = 'patlaks'

urlpatterns = [
    url(r"articles$", CompetitorViews.CompetitorList.as_view(),
        name="api-article-list"),
    url(r'fake/$', FakeViews.generateFake, name='fake'),

    url(r'competitor-list/$', CompetitorApiViews2.competitor_list, name='deneme-ssdsdsd'),

    url(r'^competitor-detail/(?P<pk>\d+)$', CompetitorViews.user_detail, name='user-detail'),

    ]