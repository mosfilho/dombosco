from django import template
from menu.models import Menu
from django.contrib.sites.models import Site
<<<<<<< HEAD
<<<<<<< HEAD
from django.template.loader import render_to_string
=======
from siteconfig.models import SiteConfig

>>>>>>> f158ccbe2cdc71801e30816132356c06033177d0
=======
from siteconfig.models import SiteConfig

>>>>>>> f158ccbe2cdc71801e30816132356c06033177d0

register = template.Library()

@register.filter
def get_submenus(parent):
    """Get parent object menu and return all childs objects"""
    return Menu.objects.filter(pagina_pai = parent, esta_publicado = True)

#@register.assignment_tag
<<<<<<< HEAD
<<<<<<< HEAD
def menu_list(context):  
    """
    return menu bootstrap
    """
    current_site = Site.objects.get_current()
    parent_menus = Menu.objects.filter(pagina_pai__isnull = True, esta_publicado = True, sites__in = [current_site])
    return {'menus'   : parent_menus,
            'request' : context['request'],
            'site'    : context['site']}
register.inclusion_tag('menu_list.html', takes_context = True) (menu_list)

@register.simple_tag
def menu_css(*args):
    """
    return a boostrap calendar tag css files
    """
    return render_to_string(
        'menu/menu_css.html'
    )
=======
=======
>>>>>>> f158ccbe2cdc71801e30816132356c06033177d0
def menu_list():  
    site = Site.objects.get_current()
    parent_menus = Menu.objects.filter(pagina_pai__isnull = True, esta_publicado = True, sites__in = [site])
    return {
        'menus' : parent_menus,
	    'site' : SiteConfig.objects.get(id = site.id),
	}
register.inclusion_tag('menu_list.html') (menu_list)
>>>>>>> f158ccbe2cdc71801e30816132356c06033177d0
