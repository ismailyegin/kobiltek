import datetime

from django import template

register = template.Library()


@register.filter
def get_at_index(list, index):
    return list[index]


@register.filter
def to_int(value):
    return int(value)


@register.filter
def is_past_due(lecture_date):
    today = datetime.datetime.now()
    lecture_date = datetime.date(int(lecture_date.year), int(lecture_date.month), int(lecture_date.day))
    current = datetime.date(int(today.year), int(today.month), int(today.day))

    return current == lecture_date
