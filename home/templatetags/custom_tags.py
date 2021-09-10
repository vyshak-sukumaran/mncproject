from django import template
from django.db.models import Avg

register = template.Library()

@register.filter(name='times') 
def times(number):
    return range(int(number))

@register.filter(name='avg')
def avg(queryset, id):
    return queryset.filter(company__id = id).aggregate(avg_value=Avg('rating')).get('avg_value')
