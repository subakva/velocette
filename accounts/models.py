from django.contrib.auth.models import User
from django.db import models

from auditable.models import AuditableModel
from auditable.managers import ActiveManager, RecentManager
from timezones.fields import TimeZoneField

class Profile(AuditableModel):
    user = models.ForeignKey(User, unique=True)
    time_zone = TimeZoneField()

    # Managers
    objects = models.Manager()
    active = ActiveManager()

    def __unicode__(self):
        return "%s: (%s)" % (self.user.username, self.time_zone,)
