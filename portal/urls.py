from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^publicacao/(?P<tipo>[\w_-]+)/(?P<slug>[\w_-]+)/$', 'portal.views.test', name='portal_test'),
)
