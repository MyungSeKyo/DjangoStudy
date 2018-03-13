from django.conf.urls import url
from bookmark.views import *

app_name = 'bookmark'

urlpatterns = [
    url(r'^$', BookmarkLV.as_view(), name='index'),
    url(r'(?P<pk>\d+)/', BookmarkDV.as_view(), name='detail'),

    url(r'^add/$', BookmarkCreateView.as_view(), name='add'),
    url(r'^change/$', BookmarkChangeLV.as_view(), name='change'),
    url(r'^(?P<pk>\d+)/update/$', BookmarkUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', BookmarkDeleteView.as_view(), name='delete'),
]
