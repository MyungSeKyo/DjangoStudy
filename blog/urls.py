from django.conf.urls import url
from blog.views import *

app_name = 'blog'

urlpatterns = [
    url(r'^$', PostLV.as_view(), name='index'),
    url(r'^post/$', PostLV.as_view(), name='post_list'),
    url(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name='post_detail'),
    url(r'^add/$', PostCreateView.as_view(), name='add'),
    url(r'^change/$', PostChangeLV.as_view(), name='change'),
    url(r'^(?P<pk>\d+)/update/$', PostUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', PostDeleteView.as_view(), name='delete'),
    url(r'^archive/$', PostAV.as_view(), name='post_archive'),
    url(r'^(?P<year>\d+)/$', PostYAV.as_view(), name='post_year_archive'),
    url(r'^(?P<year>\d+)/(?P<month>[-\w]+)/$', PostMAV.as_view(), name='post_month_archive'),
    url(r'^(?P<year>\d+)/(?P<month>[-\w]+)/(?P<day>\d+)/$', PostDAV.as_view(), name='post_day_archive'),
    url(r'^today/$', PostTAV.as_view(), name='post_today_archive'),
    url(r'^search/$', SearchFormView.as_view(), name='search'),
]
