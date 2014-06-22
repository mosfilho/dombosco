from django import template
from menu.models import Menu
from django.contrib.sites.models import Site
from ..models import Layout, TipoPublicacao, Publicacao, TabelaLayout, Tag, TagItem, Galeria
from django.contrib.contenttypes.models import ContentType
from django.template.loader import render_to_string 
from django.db.models import Q
from datetime import datetime

NUM_REGISTROS = 4

register = template.Library()

def banner_principal(context):
    """
    Include html with main banner. By default, the locale is 1
    """
    banners = []
    try:
        for layout in Layout.objects.filter(local = 1):
            table = ContentType.objects.get_for_id(layout.content_type.id)
            banners.append(table.get_object_for_this_type(pk=layout.object_id, esta_ativo = True))
            size = [layout.local.largura, layout.local.altura]
        return {'banners' : banners,
                'size' : size}
    except:
        return None
register.inclusion_tag('banner_principal.html', takes_context = True) (banner_principal)

def pub_destaque(context):
    """
    Include html with hot publications. By default, the locale is 2
    """
    object_list = []
    try:
        for layout in Layout.objects.filter(Q(data_expiracao__gte=datetime.now()) |
        	                                Q(data_expiracao__isnull=True),
        	                                local = 2):
            table = ContentType.objects.get_for_id(layout.content_type.id)
            try:
                object_list.append(table.get_object_for_this_type(esta_ativo=True, pk=layout.object_id))
            except:
            	pass
            size = [layout.local.largura, layout.local.altura]
        return {'object_list' : object_list, 
                'size' : size,
                'view' : 'destaque'}
    except:
        return None
register.inclusion_tag('pub_destaque.html', takes_context = True) (pub_destaque)

def pub_acessadas(context):
    """
    retorna as mais acessadas
    """
    try:
        local = TabelaLayout.objects.get(id = 2)
        size = [local.largura, local.altura]
        return {'object_list' : Publicacao.objects.filter(esta_ativo = True).order_by('-numeroVisitas'),
                'size' : size,
                'view' : 'acessadas'}
    except:
       return None
register.inclusion_tag('pub_destaque.html', takes_context = True) (pub_acessadas)

def pub_layout():
    """
    retorna um array de id que esta com publicacao em destaque: banner, em destaque,...
    """
    try:
        id_pub_layout = []
        table = ContentType.objects.get_for_model(Publicacao)
        banners = Layout.objects.filter(local = 1, content_type=table).order_by('-id').values('object_id')[:4]
        for banner in banners:
            id_pub_layout.append(banner['object_id'])
        pubs_destaque = Layout.objects.filter(local = 2, content_type=table).order_by('-id').values('object_id')[:4]
        for pub_destaque in pubs_destaque:
            id_pub_layout.append(pub_destaque['object_id'])
        return id_pub_layout
    except:
        return None

def pub_comum(context):
    """
    retorna todos tipo_publicacao
    """
    try:
        return {'tipos_publicacao' : TipoPublicacao.objects.filter(esta_ativo = True).order_by('ordem'),
                'teste' : pub_layout()}
    except:
        return None
register.inclusion_tag('pub_comum.html', takes_context = True) (pub_comum)

@register.filter
def pub_por_tipo(tp_pub):
    """
    por tipo_publicacao, retorna 5 publicacao ativas
    """
    return Publicacao.objects.filter(esta_ativo = True, tipo_publicacao = tp_pub).exclude(id__in = pub_layout).order_by('-data_criacao')[:5]

@register.simple_tag
def portal_css(*args):
    return render_to_string(
        'portal/portal_css.html'
    )

@register.simple_tag
def galeria_css(*args):
    return render_to_string(
        'portal/galeria_css.html'
    )

@register.filter
def get_app_label(obj):
    return ContentType.objects.get_for_model(obj)

@register.filter
def get_tags(obj):
    """ 
    return all tags related by object in param
    """
    try:
        tipo_dinamico  = ContentType.objects.get_for_model(obj)
        tag_items = TagItem.objects.filter(
            content_type=tipo_dinamico,
            object_id=obj.id)
        return [item.tag for item in tag_items]
    except:
        return False


def galeria_destaque(context):
    try:
        object_list = Galeria.objects.filter(esta_ativo = True).order_by('-id')[:4]
        local = TabelaLayout.objects.get(id = 1)
        #size = [local.largura, local.altura]
        size = [300, 200]
        return {'object_list' : object_list, 
                'size'        : size}
    except:
        return None
register.inclusion_tag('galeria_destaque.html', takes_context = True) (galeria_destaque)

@register.filter
def get_related_objects(obj):
    object_list = []
    tags = TagItem.objects.filter(object_id = obj.id)
    table_obj = ContentType.objects.get_for_model(obj)
    for tag in tags:
        table = ContentType.objects.get_for_id(tag.content_type.id)
        if table == table_obj:
            object_new = table.get_object_for_this_type(pk=tag.object_id, esta_ativo = True)
            if not obj == object_new:
                object_list.append(table.get_object_for_this_type(pk=tag.object_id, esta_ativo = True))
        else:
            object_list.append(table.get_object_for_this_type(pk=tag.object_id, esta_ativo = True))
    
    return [obj for obj in object_list]

@register.assignment_tag
def tp_publicacao():
    try:
        return [obj for obj in TipoPublicacao.objects.all()]
    except:
        return []
