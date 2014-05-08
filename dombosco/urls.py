from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dombosco.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^', include('filer.server.urls')),
<<<<<<< HEAD
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
=======
)
>>>>>>> f158ccbe2cdc71801e30816132356c06033177d0

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
		    (r'^media/(?P<path>.*)$', 'django.views.static.serve', 
			    {'document_root': settings.MEDIA_ROOT}))

