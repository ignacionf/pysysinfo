from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
admin.autodiscover()


# vacio si para acceder a pysysinfo se hace desde la misma url
BASE_URL='pysysinfo/'

urlpatterns = patterns('',
        (r'%sstatic/(?P<path>.*)$' % BASE_URL, 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	(r'^%s$' % BASE_URL, include('home.urls')),
	(r'^%shome/' % BASE_URL, include('home.urls')),
	(r'^%s__admin/(.*)' % BASE_URL, admin.site.root),
)
