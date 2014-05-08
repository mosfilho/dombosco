from django.contrib.sites.models import Site
from siteconfig.models import SiteConfig

def site(request):
    site = Site.objects.get_current()
    return {
<<<<<<< HEAD
        'site': SiteConfig.objects.get(id = site.id)
    }
=======
        'site' : SiteConfig.objects.get(id = site.id)
    }
>>>>>>> f158ccbe2cdc71801e30816132356c06033177d0
