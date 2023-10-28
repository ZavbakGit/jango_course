from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='split')
@stringfilter
def split(value, key=' '):
    return value.split(key)


@register.filter(name='times')
def times(value):
    return list(range(value))


@register.filter(name='filter_range')
def filter_range(value, end = None):
    if end is None:
        end = value + 1
    return list(range(value, end))
