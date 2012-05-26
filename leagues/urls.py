from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('leagues.views',
    url(r'^$', 'index'),
)