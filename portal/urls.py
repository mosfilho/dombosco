from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^(?P<tipo>[\w_-]+)/$', 'portal.views.tipo', name='portal_tipo'),
    url(r'^(?P<tabela>[\w_-]+)/(?P<slug>[\w_-]+)/$', 'portal.views.view', name='portal_view'),
)
