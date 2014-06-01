from django import template
from django.utils.safestring import mark_safe
from ..fullcalendar import css_url, print_css_url, javascript_url, jquery_url, jquery_ui_url
from ..util import event_url, OPTIONS_EVENT, calendar_options
from ..models import CalendarEvent
from datetime import datetime

register = template.Library()


@register.inclusion_tag("fullcalendar/calendar_list.html")
def calendar_list():
    hoje = datetime.now()
    object_list = CalendarEvent.objects.filter(start__lte = hoje, end__gte = hoje)[:5]
    month_list = CalendarEvent.objects.filter(start__month = hoje.month)[:5]
    return {'object_list':object_list}

@register.inclusion_tag("fullcalendar/calendar.html")
def calendar():
    return {}

@register.inclusion_tag("fullcalendar/calendar_init.html")
def calendar_init(calendar_config_options):
    return {'calendar_config_options': mark_safe(calendar_config_options)}

@register.simple_tag
def fullcalendar_css_url():
    return css_url()

@register.simple_tag
def fullcalendar_print_css_url():
    return print_css_url()

@register.simple_tag
def fullcalendar_javascript_url():
    return javascript_url()

@register.simple_tag
def fullcalendar_jquery_url():
    return jquery_url()

@register.simple_tag
def fullcalendar_jquery_ui_url():
    return jquery_ui_url()

@register.simple_tag
def fullcalendar_css():
    url = fullcalendar_css_url()
    return "<link href='%s' rel='stylesheet' />" % url

@register.simple_tag
def fullcalendar_print_css():
    url = fullcalendar_print_css_url()
    return "<link href='%s' rel='stylesheet' media='print' />" % url

@register.simple_tag
def fullcalendar_jquery():
    url = fullcalendar_jquery_url()
    return "<script src='%s'></script>" % url

@register.simple_tag
def fullcalendar_jquery_ui():
    url = fullcalendar_jquery_ui_url()
    return "<script src='%s'></script>" % url

@register.simple_tag
def fullcalendar_javascript():
    url = fullcalendar_javascript_url()
    return "<script src='%s'></script>" % url

@register.assignment_tag
def calendar_opt():
    return calendar_options(event_url, OPTIONS_EVENT)
