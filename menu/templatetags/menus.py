from django import template
from menu.models import Menu
from django.contrib.sites.models import Site
from siteconfig.models import SiteConfig


register = template.Library()

@register.filter
def get_submenus(parent):
    """Get parent object menu and return all childs objects"""
    return Menu.objects.filter(pagina_pai = parent, esta_publicado = True)

#@register.assignment_tag
def menu_list():  
    site = Site.objects.get_current()
    parent_menus = Menu.objects.filter(pagina_pai__isnull = True, esta_publicado = True, sites__in = [site])
    return {
        'menus' : parent_menus,
	    'site' : SiteConfig.objects.get(id = site.id),
	}
register.inclusion_tag('menu_list.html') (menu_list)
