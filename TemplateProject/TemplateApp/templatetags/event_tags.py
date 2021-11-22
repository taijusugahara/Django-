from django import template

register = template.Library()


@register.filter(name='status_to_string')
def convert_status_to_string(status):
    if status == 10:
        return 'success'
    elif status == 20:
        return 'error'
    elif status == 30:
        return 'pending'
    elif status == 50:
        return 'failed'
    else:
        return 'Unknown'
