from django import template

register = template.Library()


@register.filter
def highlight(value1, value2):
    if value2:
        return value1.replace(value2, '<span style="color:blue;">'+value2+'</span>')
    else:
        return value1

