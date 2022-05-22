from django import template
from main.models import *

register = template.Library()

@register.simple_tag()
def get_categories():
    return News.objects.all()

@register.inclusion_tag('main/simple.html')
def show_categories():
    cats = Heroes.objects.all()
    return {"cats": cats}


@register.inclusion_tag('main/simple_writers.html')
def show_categories_for_writers():
    cats = Writers.objects.all()
    return {"cats": cats}