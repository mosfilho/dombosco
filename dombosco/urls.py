from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dombosco.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^teste/$', 'portal.views.test'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^', include('filer.server.urls')),
    url(r'^portal/', include('portal.urls')),
    url(r'^tag/(?P<tag>[\w_-]+)/$', 'portal.views.tag'),
    url(r'^eventos/', 'fullcalendar.views.eventos', name='eventos'),
)


if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
		    (r'^media/(?P<path>.*)$', 'django.views.static.serve', 
			    {'document_root': settings.MEDIA_ROOT}),
		    (r'^static/(?P<path>.*)$', 'django.views.static.serve', 
			    {'document_root': settings.STATIC_ROOT}))

