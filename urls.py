from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^sessions/new/$', 'django.contrib.auth.views.login', {'SSL':True}, 'new_session'),
    (r'^sessions/create/$', 'django.contrib.auth.views.login', {'SSL':True}, 'create_session'),
    (r'^sessions/destroy/$', 'django.contrib.auth.views.logout_then_login', None, 'destroy_session'),

    (r'^accounts/', include('velocette.accounts.urls')),
    (r'^tasks/', include('velocette.tasks.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/(.*)', admin.site.root, {'SSL':True}, 'admin'),
    (r'^r/', include('django.conf.urls.shortcut')),
)
urlpatterns += patterns('django.views.generic.simple',
    (r'^$', 'direct_to_template', {'template':'welcome.html'}, 'welcome'),
)

#development
if settings.SERVE_STATIC:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/Users/jason/Code/subakva/velocette/static/'}),
    )
