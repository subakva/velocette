import datetime

from django.db import models

class ActiveManager(models.Manager):
    '''
    Custom manager that only returns active items.
    The model must have an 'is_active' column.
    '''
    def get_query_set(self):
        '''Excludes inactive items from the query set.'''
        return super(ActiveManager, self).get_query_set().filter(is_active=True)

class RecentManager(ActiveManager):
    '''
    Custom manager that only returns active items that have been modified recently.
    "Recently" is defined by the datetime.datetime.timedelta passed to the constructor.
    '''

    def __init__(self, delta, *args, **kwargs):
        self.delta = delta
        super(RecentManager, self).__init__(*args, **kwargs)

    def get_query_set(self):
        '''Excludes non-recent items from the query set.'''
        # min_modified = datetime.datetime.now()
        min_modified = datetime.datetime.now() - self.delta
        return super(RecentManager, self).get_query_set().filter(modified_at__gte=min_modified)
