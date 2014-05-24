from django.shortcuts import render
from django.http import HttpResponse
from .models import CalendarEvent
from .util import events_to_json

def eventos(request):
    events = CalendarEvent.objects.all()
    return HttpResponse(events_to_json(events), content_type='application/json')
