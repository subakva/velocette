from django.conf.urls.defaults import *

urlpatterns = patterns('velocette.tasks.views',
    (r'^$',                          'index',   None, 'tasks_index' ,),
    (r'^new/$',                      'create',  None, 'new_task'    ,),
    (r'^create/$',                   'create',  None, 'create_task' ,),
    (r'^(?P<task_id>\d+)/$',         'show',    None, 'show_task'   ,),
    (r'^(?P<task_id>\d+)/edit/$',    'update',  None, 'edit_task'   ,),
    (r'^(?P<task_id>\d+)/update/$',  'update',  None, 'update_task' ,),
    (r'^(?P<task_id>\d+)/destroy/$', 'destroy', None, 'destroy_task',),

    (r'^history/$', 'history',  None, 'task_history' ,),
    (r'^backlog/$', 'backlog',  None, 'backlog' ,),

    (r'^(?P<task_id>\d+)/backlog/$', 'backlog_task',  None, 'backlog_task' ,),
    (r'^(?P<task_id>\d+)/backlog/destroy/$', 'unbacklog_task',  None, 'unbacklog_task' ,),

    (r'^(?P<task_id>\d+)/completion/$', 'complete',  None, 'complete_task' ,),
    (r'^(?P<task_id>\d+)/completion/destroy/$', 'uncomplete',  None, 'uncomplete_task' ,),
)
