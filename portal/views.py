from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.contenttypes.models import ContentType
from models import TipoPublicacao, Publicacao
from . import get_tags

# Create your views here.
def test(request, tipo, slug):
    tipo = TipoPublicacao.objects.get(slug = tipo)
    pub = Publicacao.objects.get(slug = slug)
    tags = get_tags(pub)
    return render_to_response('conteudo.html', locals(),
        context_instance = RequestContext(request))
