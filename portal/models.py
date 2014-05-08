# -*- encoding: utf-8 -*-

from django.db import models
from django.db.models import signals
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from filer.fields.image import FilerImageField
from django.contrib.contenttypes.models import ContentType

class Agregador(models.Model):
    id = models.AutoField(primary_key = True)

    class Meta:
        verbose_name = u'Agregador de Informações'
        verbose_name_plural = u'Agregadores de Informações'


class EstruturaConteudo (models.Model):
    nome = models.CharField(max_length = 40)
    slug = models.SlugField(max_length = 55, blank = True, null = True,
        help_text = u'Identificador na URL. É gerado automaticamente ao salvar este conteúdo')
    esta_ativo = models.BooleanField(default = True)
    numeroVisitas = models.IntegerField(blank = True, null = True, editable = False)

    class Meta:
        abstract = True
        ordering = ['nome']
    
    def __unicode__(self):
        return self.nome
 
    def get_abolsute_url(self):
        return self.url
    
class TipoPublicacao (EstruturaConteudo):
    class Meta:
        verbose_name = u'Tipo de Conteúdo'
        verbose_name_plural = u'Tipos de Conteúdo'
    pass

class Galeria (EstruturaConteudo):
    class Meta:
        verbose_name = u'Galeria de Imagem'
        verbose_name_plural = u'Galerias de Imagem'
    agregador = models.ForeignKey(Agregador, null = True, blank = True, editable = False, on_delete = models.SET_NULL)

class ImagemGaleria (models.Model):
    galeria = models.ForeignKey(Galeria)
    imagem = FilerImageField()

    class Meta:
        verbose_name = u'Imagem da galeria'
        verbose_name_plural = u'Imagens da galeria'

class Publicacao (EstruturaConteudo):
    tipo_publicacao = models.ForeignKey(TipoPublicacao, null = True, blank = True, on_delete = models.SET_NULL) 
    texto = models.TextField()
    imagem_apresentacao = FilerImageField(null = True, blank = True)
    autor = models.ForeignKey(User, related_name = 'autor', editable = False, null = True, blank = True, on_delete = models.SET_NULL)
    editor = models.ForeignKey(User, related_name = 'editor', editable = False, null = True, blank = True, on_delete = models.SET_NULL)
    data_criacao = models.DateTimeField(auto_now = True, verbose_name = u'Data da Criação')
    data_edicao = models.DateTimeField(editable = False, verbose_name = u'Data da Edição', blank = True, null = True)
    agregador = models.ForeignKey(Agregador, null = True, blank = True, editable = False, on_delete = models.SET_NULL)

    class Meta:
        verbose_name = u'Publicação'
        verbose_name_plural = u'Publicações'

    def __unicode__(self):
        return self.nome

class TabelaLocal(models.Model):
    local = models.CharField(max_length = 30, help_text = u'e.g: Slideshow, Topo do Site, etc')   

    class Meta:
        verbose_name = u'Tabela do Local'
        verbose_name_plural = u'Tabelas do Local'

    def __unicode__(self):
        return self.local

class LocalPublicacao(models.Model):
    local = models.ForeignKey(TabelaLocal, null = True, blank = True, on_delete = models.SET_NULL)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField(db_index = True)

    class Meta:
        verbose_name = u'Local da Publicação'
        verbose_name_plural = u'Locais da Publicação'

# www.aprendendodjango.com.br
class Tag(models.Model):
    nome = models.CharField(max_length = 30, unique = True)

    def __unicode__(self):
        return self.nome

class TagItem(models.Model):
    tag = models.ForeignKey(Tag)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField(db_index = True)

    class Meta:
        unique_together = ('tag', 'content_type', 'object_id')

################################################## SIGNALS ###########################################################

def publicacao_pre_save(signal, instance, sender, **kwargs):
   """Este signal gera um slug automaticamente. Ele verifica se ja existe um conteudo com o mesmo 
      slug e acrescenta um numero ao final para evitar duplicidade"""
   if not instance.slug:
       slug = slugify(instance.nome)
       novo_slug = slug
       contador = 0
       while Publicacao.objects.filter(slug=novo_slug).exclude(id=instance.id).count() > 0:
           contador += 1
           novo_slug = '%s-%d'%(slug, contador)
       instance.slug = novo_slug

def tipo_publicacao_pre_save(signal, instance, sender, **kwargs):
   if not instance.slug:
       slug = slugify(instance.nome)
       novo_slug = slug
       contador = 0
       while TipoPublicacao.objects.filter(slug=novo_slug).exclude(id=instance.id).count() > 0:
           contador += 1
           novo_slug = '%s-%d'%(slug, contador)
       instance.slug = novo_slug

def galeria_pre_save(signal, instance, sender, **kwargs):
   if not instance.slug:
       slug = slugify(instance.nome)
       novo_slug = slug
       contador = 0
       while Galeria.objects.filter(slug=novo_slug).exclude(id=instance.id).count() > 0:
           contador += 1
           novo_slug = '%s-%d'%(slug, contador)
       instance.slug = novo_slug

signals.pre_save.connect(publicacao_pre_save, sender=Publicacao)
signals.pre_save.connect(tipo_publicacao_pre_save, sender=TipoPublicacao)
signals.pre_save.connect(galeria_pre_save, sender=Galeria)
