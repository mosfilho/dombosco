from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^(?P<ano>\d+)/$', 'fullcalendar.views.ver_evento'),
    url(r'^(?P<ano>\d+)/(?P<mes>\d+)/(?P<dia>\d+)/(?P<id>\d+)/$', 'fullcalendar.views.ver_evento'),
    url(r'^(?P<ano>\d+)/(?P<mes>\d+)/(?P<dia>\d+)/$', 'fullcalendar.views.ver_evento'),
    url(r'^(?P<ano>\d+)/(?P<mes>\d+)/$', 'fullcalendar.views.ver_evento'),
)
