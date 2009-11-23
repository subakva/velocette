import datetime

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models

from auditable.models import AuditableModel
from auditable.managers import ActiveManager, RecentManager
from timezones.fields import LocalizedDateTimeField

class Task(AuditableModel):
    
    description = models.TextField(max_length=140)
    estimate = models.PositiveIntegerField()
    completed_at = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User)
    backlogged = models.BooleanField()

    # Managers
    objects = models.Manager()
    active = ActiveManager()

    def is_completed(self):
        return self.completed_at is not None
    
    def get_absolute_url(self):
        return reverse('show_task', args=(self.id,))

    def __unicode__(self):
        return self.description
    