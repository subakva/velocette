from django.db import models

from auditable.fields import CreatedDateTimeField, ModifiedDateTimeField
from auditable.managers import ActiveManager

class AuditableModel(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = CreatedDateTimeField()
    modified_at = ModifiedDateTimeField()

    # Setting up the managers here does not work yet: 
    # http://code.djangoproject.com/ticket/7252
    # http://code.djangoproject.com/ticket/7154
    # 
    # unfiltered = models.Manager()
    # objects = ActiveManager()

    class Meta:
        abstract = True
        get_latest_by = 'created_at'
        ordering = ['-created_at','-id']
    