# -*- encoding: utf-8 -*-
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class DataEvento(models.Model):
    cod_data_evento = models.IntegerField(primary_key = True, db_index = True)
    data = models.DateTimeField(blank=True, null=True)
    cod_publicacao = models.IntegerField(blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True)
    feriado = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'data_evento'

class Menu(models.Model):
    cod_menu = models.IntegerField(primary_key = True, db_index = True)
    titulo = models.CharField(max_length=200, blank=True)
    texto = models.TextField(blank=True)
    cod_menu_pai = models.IntegerField(blank=True, null=True)
    ativo = models.BooleanField()
    link = models.CharField(max_length=256, blank=True)

    class Meta:
        managed = False
        db_table = 'menu'

class Publicacao(models.Model):
    cod_publicacao = models.IntegerField(primary_key = True, db_index = True)
    album = models.BooleanField()
    arquivo = models.BooleanField()
    blog = models.NullBooleanField()
    data = models.DateField(blank=True, null=True)
    destaque = models.NullBooleanField()
    feriado = models.NullBooleanField()
    imagem = models.BooleanField()
    texto = models.TextField(blank=True)
    cod_tipo_publicacao = models.ForeignKey(TipoPublicacao, on_delete = models.SET_NULL)
    titulo = models.CharField(max_length=255, blank=True)
    cod_usuario = models.IntegerField(blank=True, null=True)
    numvisitas = models.IntegerField(blank=True, null=True)
    subtitulo = models.CharField(max_length=256, blank=True)

    class Meta:
        managed = False
        db_table = 'publicacao'

class PublicacaoSerie(models.Model):
    cod_publicacao_serie = models.IntegerField(primary_key = True, db_index = True)
    cod_serie = models.IntegerField(blank=True, null=True)
    cod_publicacao = models.ForeignKey(Publicacao, blank=True, null=True, on_delete = models.SET_NULL)

    class Meta:
        managed = False
        db_table = 'publicacao_serie'

class TipoPublicacao(models.Model):
    cod_tipo_publicacao = models.IntegerField(primary_key = True)
    descricao = models.CharField(max_length=256, blank=True)

    class Meta:
        managed = False
        db_table = 'tipo_publicacao'

class Usuario(models.Model):
    cod_usuario = models.IntegerField(primary_key = True, db_index = True)
    data_cadastro = models.DateTimeField(blank=True, null=True)
    login = models.CharField(max_length=255, blank=True)
    nome = models.CharField(max_length=255, blank=True)
    senha = models.CharField(max_length=255, blank=True)
    cargo = models.CharField(max_length=255, blank=True)
    sobre = models.CharField(max_length=255, blank=True)
    admin = models.NullBooleanField()
    blogger = models.NullBooleanField()
    editor = models.NullBooleanField()
    manager = models.NullBooleanField()
    publisher = models.NullBooleanField()
    foto = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'usuario'
        verbose_name = u'Usuário'
        verbose_name_plural = u'Usuários'

