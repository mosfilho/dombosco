# -*- encoding: utf-8 -*-

from django.contrib import admin
from models import SiteConfig
from django.contrib.sites.admin import SiteAdmin
from django.contrib.sites.models import Site

class SiteConfigAdmin(admin.ModelAdmin):
    list_display = ('domain', 'name')
    search_fields = ('domain', 'name')
    fieldsets = (
    	(None, {'fields' : ('domain', 'name', 'slogan', 'descricao') } ),
    	('Redes Sociais', { 'fields' : ('facebook_id','twitter_site')} ),
    	(u'Mídias', {'fields' : ('logo_menu','imagem_site')} ),
    )

admin.site.unregister(Site)
admin.site.register(SiteConfig, SiteConfigAdmin)
