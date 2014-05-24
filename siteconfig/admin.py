# -*- encoding: utf-8 -*-

from django.contrib import admin
from models import SiteConfig
from django.contrib.sites.admin import SiteAdmin
from django.contrib.sites.models import Site

#admin.site.unregister(Site)
admin.site.register(SiteConfig)
