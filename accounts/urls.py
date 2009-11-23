from django.conf.urls.defaults import *

urlpatterns = patterns('velocette.accounts.views',
    # (r'^$',                             'index',   None, 'accounts_index' ,),
    # (r'^(?P<account_id>\d+)/$',         'update',  None, 'show_account'   ,),
    # (r'^(?P<account_id>\d+)/destroy/$', 'destroy', None, 'destroy_account',),
    (r'^new/$',                         'create',  {'SSL':True}, 'new_account'    ,),
    (r'^create/$',                      'create',  {'SSL':True}, 'create_account' ,),
    (r'^(?P<account_id>\d+)/edit/$',    'update',  {'SSL':True}, 'edit_account'   ,),
    (r'^(?P<account_id>\d+)/update/$',  'update',  {'SSL':True}, 'update_account' ,),
    (r'^(?P<account_id>\d+)/password/change/$', 'change_password',  {'SSL':True}, 'change_password' ,),
)
urlpatterns += patterns('django.contrib.auth.views',
    (r'^password/reset/$', 'password_reset',  {'SSL':True}, 'password_reset' ,),
    (r'^password/reset/confirmation/$', 'password_reset_done', None, 'password_reset_done' ,),
    (r'^password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'password_reset_confirm', None, 'password_reset_confirm' ,),
    (r'^password/reset/complete/$', 'password_reset_complete', None, 'password_reset_complete' ,),
)
