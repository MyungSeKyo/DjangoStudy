from django.conf.urls import url
from photo.views import *

app_name = 'photo'

urlpatterns = [
    url(r'^$', AlbumLV.as_view(), name='index'),
    url(r'^album/$', AlbumLV.as_view(), name='album_list'),
    url(r'^album/(?P<pk>\d+)/$', AlbumDV.as_view(), name='album_detail'),
    url(r'^photo/(?P<pk>\d+)/$', PhotoDV.as_view(), name='photo_detail'),
]
