'''Contains custom Model field definitions.'''
import datetime
from django.db import models

class ModifiedDateTimeField(models.DateTimeField):
    '''A DateTimeField that always saves the current time to the database.'''
    def __init__(self, *args, **kwargs):
        kwargs['editable'] = False
        kwargs['blank'] = True
        super(ModifiedDateTimeField, self).__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        value = datetime.datetime.now()
        setattr(model_instance, self.attname, value)
        return value

class CreatedDateTimeField(models.DateTimeField):
    '''A DateTimeField that saves the current time to the database when the object is first created.'''
    def __init__(self, *args, **kwargs):
        kwargs['editable'] = False
        kwargs['blank'] = True
        super(CreatedDateTimeField, self).__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        if add:
            value = datetime.datetime.now()
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super(CreatedDateTimeField, self).pre_save(model_instance, add)


