from django.contrib.sites.models import Site
from siteconfig.models import SiteConfig

def site(request):
    site_abs = Site.objects.get_current()
    try:
        site = SiteConfig.objects.get(id = site_abs.id)
    except:
        site = None
    return { 'site': site }
