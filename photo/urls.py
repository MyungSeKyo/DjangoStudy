from django.conf.urls import url
from photo.views import *

app_name = 'photo'

urlpatterns = [
    url(r'^$', AlbumLV.as_view(), name='index'),
    url(r'^album/$', AlbumLV.as_view(), name='album_list'),
    url(r'^album/(?P<pk>\d+)/$', AlbumDV.as_view(), name='album_detail'),
    url(r'^photo/(?P<pk>\d+)/$', PhotoDV.as_view(), name='photo_detail'),
    url(r'album/add$', AlbumPhotoCV.as_view(), name='album_add'),
    url(r'album/change$', AlbumChangeLV.as_view(), name='album_change'),
    url(r'album/(?P<pk>\d+)/update/$', AlbumPhotoUV.as_view(), name='album_update'),
    url(r'album/(?P<pk>\d+)/delete/$', AlbumDeleteView.as_view(), name='album_delete'),
    url(r'photo/add$', PhotoCreateView.as_view(), name='photo_add'),
    url(r'photo/change$', PhotoChangeLV.as_view(), name='photo_change'),
    url(r'photo/(?P<pk>\d+)/update/$', PhotoUpdateView.as_view(), name='photo_update'),
    url(r'photo/(?P<pk>\d+)/delete/$', PhotoDeleteView.as_view(), name='photo_delete'),
]
