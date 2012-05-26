from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('schedule.views',
    url(r'^$', 'index'),
    url(r'^score/', 'submit_score')
)