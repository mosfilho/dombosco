# -*- encoding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
import portal


class CalendarEvent(models.Model):
    """The event set a record for an 
    activity that will be scheduled at a 
    specified date and time. 
    
    It could be on a date and time 
    to start and end, but can also be all day.
    
    :param title: Title of event
    :type title: str.
    
    :param start: Start date of event
    :type start: datetime.
    
    :param end: End date of event
    :type end: datetime.
    
    :param all_day: Define event for all day
    :type all_day: bool.
    """
    title = models.CharField(_('Title'), max_length=200)
    start = models.DateTimeField(_('Start'))
    end = models.DateTimeField(_('End'))
    all_day = models.BooleanField(_('All day'), default=False)
    text = models.TextField(blank = True, null = True)
    feriado = models.BooleanField()
    url = models.CharField(max_length = 200, null = True, blank = True)

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')

    def __unicode__(self):
        return "%s %s" %(self.title, self.start)

    def get_absolute_url(self):
        return "/evento/%s/%s/%s/%s/" % (self.start.year, self.start.month, self.start.day, self.id)

    def get_agregate(self):
        publicacoes = []
        eventos = []
        galerias = []
        if portal.models.Agregador.objects.filter(evento = self.id).exists():
            agrs = portal.models.Agregador.objects.filter(evento = self.id)
            for agr in agrs:
                try:
                    publicacoes.append(portal.models.Publicacao.objects.get(id = agr.publicacao.id))
                except:
                    pass
                try:
                    galerias.append(portal.models.Galeria.objects.get(id = agr.galeria.id))
                except:
                    pass

        return publicacoes, eventos, galerias
