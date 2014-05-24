# -*- encoding: utf-8 -*-

from django.db import models
from django.db.models import signals
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from filer.fields.image import FilerImageField
from django.contrib.contenttypes.models import ContentType
from easy_thumbnails.files import get_thumbnailer
from django.conf import settings
from paintstore.fields import ColorPickerField


class Agregador(models.Model):
    id = models.AutoField(primary_key = True)

    class Meta:
        verbose_name = u'Agregador de Informações'
        verbose_name_plural = u'Agregadores de Informações'

    def __unicode__(self):
    	try:
    	    pub = Publicacao.objects.get(agregador = self.id)
    	except:
    	    pub = None
    	try:
       	    galeria = Galeria.objects.get(agregador = self.id)
    	except:
    	    galeria = None
    	try:
    	    evento = CalendarEvent.objects.get(agregador = self.id)
    	except:
    	    evento = None

    	return "cod. %s - Public.: %s, Galeria: %s, Evento: %s" % (self.id, pub, galeria, evento)


class EstruturaConteudo (models.Model):
    nome = models.CharField(max_length = 70)
    slug = models.SlugField(max_length = 100, blank = True, null = True,
        help_text = u'Identificador na URL. É gerado automaticamente ao salvar este conteúdo')
    esta_ativo = models.BooleanField(default = True)
    numeroVisitas = models.IntegerField(blank = True, null = True, editable = False, default = 0)
    autor = models.ForeignKey(User, editable = False, null = True, blank = True, on_delete = models.SET_NULL)
    data_criacao = models.DateTimeField(verbose_name = u'Data da Criação', editable = False)

    class Meta:
        abstract = True
        ordering = ['nome']
    
    def __unicode__(self):
        return self.nome
 
    def get_absolute_url(self):
        table = ContentType.objects.get_for_model(self)
        return "/%s/%s/%s/" %(slugify(table.app_label),slugify(table.model), self.slug)

    def incrementa_visita(self):
        self.numeroVisitas += 1
        self.save()
    
class TipoPublicacao (EstruturaConteudo):
    ordem = models.IntegerField()
    cor  = ColorPickerField()
    classe_icone = models.CharField(max_length = 50, blank = True, null = True)

    class Meta:
        verbose_name = u'Tipo de Publicação'
        verbose_name_plural = u'Tipos de Publicação'

    def get_absolute_url(self):
        return "/portal/%s/" % self.slug
 
class Galeria (EstruturaConteudo):
    class Meta:
        verbose_name = u'Galeria de Imagem'
        verbose_name_plural = u'Galerias de Imagem'
    agregador = models.ForeignKey(Agregador, null = True, blank = True, editable = False, on_delete = models.SET_NULL)

    def get_image(self):
        first_image = ImagemGaleria.objects.filter(galeria = self.id)[0]
        return first_image.imagem

    def get_all_images(self):
        return ImagemGaleria.objects.filter(galeria = self.id)

    def get_url_image(self):
    	return "%s%s" %(settings.MEDIA_URL, get_thumbnailer(self.get_image()))

class ImagemGaleria (models.Model):
    galeria = models.ForeignKey(Galeria)
    imagem = FilerImageField()

    class Meta:
        verbose_name = u'Imagem da galeria'
        verbose_name_plural = u'Imagens da galeria'

    def get_url_image(self):
        return "%s%s" %(settings.MEDIA_URL, get_thumbnailer(self.imagem))


class Publicacao (EstruturaConteudo):
    tipo_publicacao = models.ForeignKey(TipoPublicacao, null = True, blank = True, on_delete = models.SET_NULL) 
    texto = models.TextField()
    imagem_apresentacao = FilerImageField(null = True, blank = True)
    agregador = models.ForeignKey(Agregador, null = True, blank = True, editable = False, on_delete = models.SET_NULL)

    class Meta:
        verbose_name = u'Publicação'
        verbose_name_plural = u'Publicações'

    def __unicode__(self):
        return self.nome
 
    def get_image(self):
    	return self.imagem_apresentacao

    def get_url_image(self):
    	return "%s%s" %(settings.MEDIA_URL, get_thumbnailer(self.imagem_apresentacao))

class TabelaLayout(models.Model):
    local = models.CharField(max_length = 30, help_text = u'e.g: Banner, Em destaque, etc')   
    largura = models.IntegerField(help_text=u'Largura em pixels da imagem de apresentação (caso houver)')
    altura = models.IntegerField(help_text=u'Altura em pixels da imagem de apresentação (caso houver)')
    tem_imagem = models.BooleanField()

    class Meta:
        verbose_name = u'Tabela de Layout'
        verbose_name_plural = u'Tabela de Layouts'

    def __unicode__(self):
        return self.local

class Layout(models.Model):
    local = models.ForeignKey(TabelaLayout, null = True, blank = True, on_delete = models.SET_NULL)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField(db_index = True)
    data_expiracao = models.DateTimeField(null = True, blank = True)

    class Meta:
        verbose_name = u'Layout'
        verbose_name_plural = u'Layouts'

# www.aprendendodjango.com.br
class Tag(models.Model):
    nome = models.CharField(max_length = 30, unique = True)
    slug = models.SlugField(max_length = 100, blank = True, null = True,
        help_text = u'Identificador na URL. É gerado automaticamente ao salvar este conteúdo')

    def __unicode__(self):
        return self.nome

    def get_absolute_url(self):
        return "/tag/%s/" % (self.slug)

class TagItem(models.Model):
    tag = models.ForeignKey(Tag)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField(db_index = True)

    class Meta:
        unique_together = ('tag', 'content_type', 'object_id')

################################################## SIGNALS ###########################################################

def tags_pre_save(signal, instance, sender, **kwargs):
   """Este signal gera um slug automaticamente. Ele verifica se ja existe um conteudo com o mesmo 
      slug e acrescenta um numero ao final para evitar duplicidade"""
   if not instance.slug:
       slug = slugify(instance.nome)
       novo_slug = slug
       contador = 0
       while Tag.objects.filter(slug=novo_slug).exclude(id=instance.id).count() > 0:
           contador += 1
           novo_slug = '%s-%d'%(slug, contador)
       instance.slug = novo_slug

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
signals.pre_save.connect(tags_pre_save, sender=Tag)
