from django import template
from menu.models import Menu
from django.contrib.sites.models import Site
from ..models import Layout, TipoPublicacao, Publicacao
from django.contrib.contenttypes.models import ContentType
from django.template.loader import render_to_string 

NUM_REGISTROS = 4

register = template.Library()

'''
@register.filter
def get_submenus(parent):
    """Get parent object menu and return all childs objects"""
    return Menu.objects.filter(pagina_pai = parent, esta_publicado = True)

#@register.assignment_tag
def menu_list():  
    current_site = Site.objects.get_current()
    parent_menus = Menu.objects.filter(pagina_pai__isnull = True, esta_publicado = True, sites__in = [current_site])
    return {'menus' : parent_menus}
register.inclusion_tag('menu_list.html') (menu_list)
'''

def main_banner(context):
    """
    Include html with main banner. By default, the locale is 1
    """
    banners = []
    for layout in Layout.objects.filter(local = 1):
        table = ContentType.objects.get_for_id(layout.content_type.id)
        banners.append(table.get_object_for_this_type(pk=layout.object_id))
        size = [layout.local.largura, layout.local.altura]
    return {'banners' : banners,
            'size' : size}
register.inclusion_tag('main_banner.html', takes_context = True) (main_banner)

def pub_destaque(context):
    """
    Include html with hot publications. By default, the locale is 2
    """
    publicacoes = []
    for layout in Layout.objects.filter(local = 2):
        table = ContentType.objects.get_for_id(layout.content_type.id)
        publicacoes.append(table.get_object_for_this_type(pk=layout.object_id))
        size = [layout.local.largura, layout.local.altura]
    return {'publicacoes' : publicacoes, 
            'size' : size}
register.inclusion_tag('pub_destaque.html', takes_context = True) (pub_destaque)

def pub_layout():
    ctype = ContentType.objects.get(model='Publicacao')
    return [ctype.objects.all().value('id')]

def pub_comum(context):
    """
    retorna todos tipo_publicacao
    """
    return {'tipos_publicacao' : TipoPublicacao.objects.all()}
register.inclusion_tag('pub_comum.html', takes_context = True) (pub_comum)

@register.filter
def pub_por_tipo(tp_pub):
    """
    por tipo_publicacao, retorna 5 publicacao ativas
    """
    return Publicacao.objects.filter(esta_ativo = True, tipo_publicacao = tp_pub).order_by('-data_edicao')[:5]

@register.simple_tag
def portal_css(*args):
    return render_to_string(
        'portal/portal_css.html'
    )

