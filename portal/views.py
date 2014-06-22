# -*- encoding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.contenttypes.models import ContentType
from models import TipoPublicacao, Publicacao, Tag, TagItem, Galeria
from django.core.paginator import Paginator

# Create your views here.
def test(request):
    return render_to_response('test.html', locals(),
        context_instance = RequestContext(request))

# Create your views here.
def view(request, tabela, slug):
    table = ContentType.objects.get(model = tabela)
    obj = table.get_object_for_this_type(slug = slug)
    obj.incrementa_visita()
    return render_to_response('conteudo.html', locals(),
        context_instance = RequestContext(request))

def tag(request, tag):
    tag = Tag.objects.get(slug = tag)
    object_list  = []
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

    mensagem = 'Tag: <small>%s</small>'%(tag.tag.nome)

    return render_to_response('lista.html', locals(),
        context_instance = RequestContext(request))

def publicacao(request):
    object_list  = Publicacao.objects.filter(esta_ativo = True).order_by('-id')
    mensagem = 'Publicações'
        
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

    return render_to_response('lista.html', locals(),
        context_instance = RequestContext(request))

def tipo(request, tipo):
    try:
        tipo = TipoPublicacao.objects.get(slug = tipo)
        object_list  = tipo.publicacao_set.filter(esta_ativo = True)
        mensagem = 'Tipo: <small>%s</small>'%(tipo.nome)
    except:
        object_list  = Galeria.objects.filter(esta_ativo = True).order_by('-id')
        mensagem = 'Galerias'
        
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

    return render_to_response('lista.html', locals(),
        context_instance = RequestContext(request))
