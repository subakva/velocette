import datetime
import pytz

from django import forms

from timezones.utils import adjust_datetime_to_timezone

from velocette.tasks.models import Task

class CreateTaskForm(forms.Form):
    description = forms.CharField(max_length=140, widget=forms.Textarea())
    estimate = forms.IntegerField(min_value=0)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(CreateTaskForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        task = Task(
            description = self.cleaned_data['description'],
            estimate = self.cleaned_data['estimate'],
            user = self.user
        )
        if commit:
            task.save()
        return task

class UpdateTaskForm(forms.Form):
    description = forms.CharField(max_length=140, widget=forms.Textarea())
    estimate = forms.IntegerField(min_value=0)
    completed_at = forms.DateTimeField(required=False)

    def __init__(self, task, *args, **kwargs):
        self.task = task
        kwargs['initial'] = {
            'description': self.task.description,
            'estimate': self.task.estimate,
            'completed_at': self.task.completed_at
        }
        super(UpdateTaskForm, self).__init__(*args, **kwargs)

    def clean_completed_at(self):
        value = self.cleaned_data['completed_at']
        if value is None:
            return value

        time_zone = self.task.user.get_profile().time_zone
        localtime = value.replace(tzinfo=pytz.timezone(time_zone))
        utctime = adjust_datetime_to_timezone(localtime, time_zone, 'UTC')
        utctime_raw = utctime.replace(tzinfo=None)
        return utctime_raw

    def save(self, commit=True):
        self.task.description = self.cleaned_data['description']
        self.task.estimate = self.cleaned_data['estimate']
        self.task.completed_at = self.cleaned_data['completed_at']

        if commit:
            self.task.save()
        return self.task
        