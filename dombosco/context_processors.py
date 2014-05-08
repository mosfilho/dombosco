from django.contrib.sites.models import Site
from siteconfig.models import SiteConfig

def site(request):
    site = Site.objects.get_current()
    return {
        'site': SiteConfig.objects.get(id = site.id)
    }
