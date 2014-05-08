# -*- encoding: utf-8 -*-

from django.contrib import admin
from models import Menu
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import ugettext_lazy as _
from redactor.widgets import RedactorEditor

class MenuForm(FlatpageForm):
    class Meta:
        model = Menu

class MenuAdmin(FlatPageAdmin):
    form = MenuForm
    fieldsets = (
        (None, {'fields': ('url', 'title', 'pagina_pai', 'sites', 'esta_publicado')}),
        ((u'Páginas Estáticas: ferramentas avançadas'), {'classes': ('collapse',), 'fields': ('content','enable_comments', 'registration_required', 'template_name')}),
    )
    list_display = ('title', 'url', 'pagina_pai', 'esta_publicado', 'template_name')
    #list_filter = ('sites', 'enable_comments', 'registration_required')
    list_filter = ('sites', 'enable_comments')
    search_fields = ('url', 'title')

# Register your models here.

admin.site.unregister(FlatPage)
admin.site.register(Menu, MenuAdmin)
