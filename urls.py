from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
        (r'static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	(r'^$', include('home.urls')),
	(r'^home/', include('home.urls')),
	(r'^__admin/(.*)', admin.site.root),
)
