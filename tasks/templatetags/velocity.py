from django import template

register = template.Library()

@register.simple_tag
def velocity(task_list):
    return sum([task.estimate for task in task_list])
