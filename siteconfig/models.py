# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.sites.models import Site
from filer.fields.image import FilerImageField
from django.utils.safestring import mark_safe
from django.conf import settings
from easy_thumbnails.files import get_thumbnailer

class SiteConfig(Site):
    facebook_id = models.CharField(max_length = 200, blank = True, null = True )
    twitter_site = models.CharField(max_length = 200, blank = True, null = True )
    logo_menu = FilerImageField(null = True, blank = True, on_delete = models.SET_NULL,
    	related_name = 'menu')
    imagem_site = FilerImageField(null = True, blank = True, on_delete = models.SET_NULL,
    	related_name = 'site')
    slogan = models.CharField(max_length = 100, null = True, blank = True)
    descricao = models.CharField(max_length = 200, blank = True, null = True)

    class Meta:
        verbose_name = u'Site'
        verbose_name_plural = u'Sites'

    def get_safe_img_logo(self):
        return mark_safe("<img src='%s%s'") % (settings.MEDIA_URL, get_thumbnailer(self.logo_menu))

    def get_url_logo(self):
        return "%s%s" % (settings.MEDIA_URL, get_thumbnailer(self.logo_menu))

    def get_logo_url(self):
        return '%s%s' %(settings.MEDIA_URL, get_thumbnailer(self.logo_menu))

