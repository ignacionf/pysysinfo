from django.conf import settings
from datetime import datetime

from django.contrib.sites.models import Site

def globales(request):

	site = Site.objects.get(pk=settings.SITE_ID)

	opciones = {
		'site': site,
		'media_url': "%s/%s" %(site.domain, settings.MEDIA_URL),
		'request': request,
		'path': "%s%s" %(settings.URL_PATH_BASE,request.META['PATH_INFO']),
		'auth': request.user.is_authenticated(),
		'now': datetime.now(),
		}

	return opciones
