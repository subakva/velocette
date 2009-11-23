from django.contrib import admin

from velocette.tasks.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('description', 'estimate', 'created_at', 'completed_at')

admin.site.register(Task, TaskAdmin)
