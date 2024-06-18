from django import template
from django.template.defaultfilters import register

registers = template.Library()


@register.filter(name="dict_reader")
def dict_reader(h, key):
    return h[key]


registers.filter("dict_reader", dict_reader)
