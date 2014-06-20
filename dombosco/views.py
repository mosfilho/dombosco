# -*- encoding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.contenttypes.models import ContentType
from portal.models import TipoPublicacao, Publicacao, Tag, TagItem, Galeria
from django.core.paginator import Paginator

def home(request):
    return render_to_response('home.html', locals(), 
        context_instance = RequestContext(request))

def buscar(request):
    key = request.GET.get('q')
    object_list  = []

    if Publicacao.objects.filter(nome__contains = key, esta_ativo = True).exists():
        for pub in Publicacao.objects.filter(nome__contains = key, esta_ativo = True):
            object_list.append(pub)

    if Galeria.objects.filter(nome__contains = key, esta_ativo = True).exists():
        for gal in Galeria.objects.filter(nome__contains = key, esta_ativo = True):
            object_list.append(gal)

    if Tag.objects.filter(slug = key).exists():
        tag = Tag.objects.get(slug = key)
        for tag in tag.tagitem_set.all():
    	    try:
                object_list.append(tag.content_type.get_object_for_this_type(id = tag.object_id, esta_ativo = True))
            except:
                pass

    paginator = Paginator(object_list, 25)
    try:
        page = request.GET.get('p','1')
    except ValueError:
        page = 1
     
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        objects = paginator.page(paginator.num_pages)

    mensagem = 'Pesquisa: <small>%s</small>'%(key)

    return render_to_response('lista.html', locals(),
        context_instance = RequestContext(request))
