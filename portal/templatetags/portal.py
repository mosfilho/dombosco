from django import template
from menu.models import Menu
from django.contrib.sites.models import Site
from ..models import Layout, TipoPublicacao, Publicacao
from django.contrib.contenttypes.models import ContentType
from django.template.loader import render_to_string 

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
            banners.append(table.get_object_for_this_type(pk=layout.object_id))
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
    publicacoes = []
    try:
        for layout in Layout.objects.filter(local = 2):
            table = ContentType.objects.get_for_id(layout.content_type.id)
            publicacoes.append(table.get_object_for_this_type(pk=layout.object_id))
            size = [layout.local.largura, layout.local.altura]
        return {'publicacoes' : publicacoes, 
                'size' : size}
    except:
        return None
register.inclusion_tag('pub_destaque.html', takes_context = True) (pub_destaque)

def pub_layout():
    """
    retorna um array de id que esta com publicacao em destaque: banner, em destaque,...
    """
    id_pub_layout = []
    table = ContentType.objects.get_for_model(Publicacao)
    banners = Layout.objects.filter(local = 1, content_type=table).order_by('-id').values('object_id')[:4]
    for banner in banners:
        id_pub_layout.append(banner['object_id'])
    pubs_destaque = Layout.objects.filter(local = 2, content_type=table).order_by('-id').values('object_id')[:4]
    for pub_destaque in pubs_destaque:
        id_pub_layout.append(pub_destaque['object_id'])
    return id_pub_layout

def pub_comum(context):
    """
    retorna todos tipo_publicacao
    """
    return {'tipos_publicacao' : TipoPublicacao.objects.all(),
            'teste' : pub_layout()}
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

