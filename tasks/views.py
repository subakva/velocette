import datetime

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic.list_detail import object_list

from timezones.utils import adjust_datetime_to_timezone, localtime_for_timezone

from velocette.tasks.models import Task
from velocette.tasks.forms import CreateTaskForm, UpdateTaskForm

DEFAULT_PAGE_SIZE = 30
DEFAULT_DAYS_BACK = 4

@login_required
def index(request):
    time_zone = request.user.get_profile().time_zone
    localtime = localtime_for_timezone(datetime.datetime.now(),time_zone)
    start_of_today = localtime.replace(hour=0,minute=0,second=0,microsecond=0)
    start_of_today_utc = adjust_datetime_to_timezone(start_of_today, time_zone, 'UTC')
    start_of_today_utc_raw = start_of_today_utc.replace(tzinfo=None)

    pending_tasks = Task.active.filter(
        user = request.user,
        completed_at__isnull = True,
        backlogged = False
    ).order_by('-created_at')

    completed_today = Task.active.filter(
        user = request.user,
        completed_at__gte = start_of_today_utc_raw
    ).order_by('-created_at')

    if request.REQUEST.has_key('days_back') and request.REQUEST['days_back'].isdigit():
        days_back = int(request.REQUEST['days_back']) + 1
    else:
        days_back = DEFAULT_DAYS_BACK

    completed_lists = [
        Task.active.filter(
            user = request.user,
            completed_at__gte = start_of_today_utc_raw - datetime.timedelta(days=delta),
            completed_at__lt = start_of_today_utc_raw - datetime.timedelta(days=delta) + datetime.timedelta(days=1)
        ).order_by('-created_at')
        for delta in range(1, days_back)
    ]

    return render_to_response('tasks/index.html',
        {
            'time_zone': time_zone,
            'new_task_form' : CreateTaskForm(request.user),
            'pending_tasks' : pending_tasks,
            'completed_today' : completed_today,
            'completed_lists': completed_lists
        },
        context_instance=RequestContext(request)
    )

@login_required
def history(request):
    time_zone = request.user.get_profile().time_zone
    tasks = Task.active.filter(user = request.user).exclude(
        completed_at = None
    ).order_by('-created_at')
    list_dict = {
        'queryset': tasks,
        'template_object_name': 'task',
        'paginate_by': DEFAULT_PAGE_SIZE,
        'extra_context': {'time_zone': time_zone,},
        'template_name': 'tasks/history.html',
    }

    return object_list(request, **list_dict)
    
@login_required
def backlog(request):
    time_zone = request.user.get_profile().time_zone
    tasks = Task.active.filter(
        user = request.user,
        backlogged = True,
        completed_at = None
    ).order_by('-created_at')
    list_dict = {
        'queryset': tasks,
        'template_object_name': 'task',
        'paginate_by': DEFAULT_PAGE_SIZE,
        'extra_context': {'time_zone': time_zone,},
        'template_name': 'tasks/backlog.html',
    }
    return object_list(request, **list_dict)

@login_required
def create(request):
    if request.method == 'POST':
        form = CreateTaskForm(request.user, request.POST)
        if form.is_valid():
            task = form.save()
            # TODO: add a session variable for "recently_added" to mark it in the list
            request.notifications.create("Created task: %s" % task.description)
            return HttpResponseRedirect(reverse('tasks_index'))
    else:
        form = CreateTaskForm(request.user)

    template = request.is_xhr and 'tasks/forms/_new.html' or 'tasks/new.html'
    return render_to_response(template, { 'new_task_form':form },
        context_instance=RequestContext(request))

@login_required
def show(request, task_id):
    task = get_object_or_404(Task.active, pk=task_id, user = request.user)
    return render_to_response('tasks/show.html',
        { 'task': task },
        context_instance=RequestContext(request)
    )

@login_required
def update(request, task_id):
    task = get_object_or_404(Task.active, pk=task_id, user = request.user)
    if request.method == 'POST':
        form = UpdateTaskForm(task, request.POST)
        if form.is_valid():
            task = form.save()
            # TODO: add a session variable for "recently_edited" to mark it in the list
            request.notifications.create("Updated task: %s" % task.description)
            return HttpResponseRedirect(reverse('tasks_index'))
    else:
        form = UpdateTaskForm(task)

    template = request.is_xhr and 'tasks/forms/_edit.html' or 'tasks/edit.html'
    return render_to_response(template, { 'task':task, 'edit_task_form':form },
        context_instance=RequestContext(request))

@login_required
def backlog_task(request, task_id):
    task = get_object_or_404(Task.active, pk=task_id, user = request.user)
    task.backlogged = True
    task.save()
    request.notifications.create("Backlogged task: %s" % task.description)
    return HttpResponseRedirect(reverse('tasks_index'))

@login_required
def unbacklog_task(request, task_id):
    task = get_object_or_404(Task.active, pk=task_id, user = request.user)
    task.backlogged = False
    task.save()
    request.notifications.create("Pending task: %s" % task.description)
    return HttpResponseRedirect(reverse('backlog'))

@login_required
def uncomplete(request, task_id):
    task = get_object_or_404(Task.active, pk=task_id, user = request.user)
    task.completed_at = None
    task.save()
    # TODO: add a session variable for "recently_uncompleted" to mark it in the list
    request.notifications.create("Pending task: %s" % task.description)
    return HttpResponseRedirect(reverse('tasks_index'))

@login_required
def complete(request, task_id):
    task = get_object_or_404(Task.active, pk=task_id, user = request.user)
    task.completed_at = datetime.datetime.now()
    task.save()
    # TODO: add a session variable for "recently_completed" to mark it in the list
    request.notifications.create("Completed task: %s" % task.description)
    return HttpResponseRedirect(reverse('tasks_index'))

@login_required
def destroy(request, task_id):
    task = get_object_or_404(Task.active, pk=task_id, user = request.user)
    if request.method == 'POST':
        task.is_active = False
        task.save()
        request.notifications.create("Removed task: %s" % task.description)
        return HttpResponseRedirect(reverse('tasks_index'))
    else:
        template = request.is_xhr and 'tasks/forms/_destroy.html' or 'tasks/destroy.html'
        return render_to_response(template, { 'task':task },
            context_instance=RequestContext(request))
