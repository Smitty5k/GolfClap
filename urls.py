from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib.auth.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'GolfClap.views.home', name='home'),
    # url(r'^GolfClap/', include('GolfClap.foo.urls')),
    url(r'^$', 'schedule.views.index'),
    url(r'^leagues/', include('leagues.urls')),
    url(r'^schedule/', include('schedule.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout),
    url(r'^accounts/profile/$', 'schedule.views.index'),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )