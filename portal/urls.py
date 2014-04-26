from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'portal.views.test', name='portal_test'),
    url(r'^galeria/$', 'portal.views.gallery_test', name='gallery_test'),
)
