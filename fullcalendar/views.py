from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from models import CalendarEvent
from util import events_to_json

def eventos(request):
    events = CalendarEvent.objects.all()
    return HttpResponse(events_to_json(events), content_type='application/json')

def ver_evento(request, ano = None, mes = None, dia = None, id = None):
    object_list = []
    if ano is not None:
        object_list = CalendarEvent.objects.filter(start__year = ano)
    if mes is not None:
        object_list = CalendarEvent.objects.filter(start__month = mes)
    if dia is not None:
        object_list = CalendarEvent.objects.filter(start__day = mes)
    if id is not None:
        object_list = CalendarEvent.objects.filter(id = id)

    return render_to_response('eventos.html', locals(),
        context_instance = RequestContext(request))
    
def calendario(request):
    return render_to_response('calendario.html', locals(),
        context_instance = RequestContext(request))
