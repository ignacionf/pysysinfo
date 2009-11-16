# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
        (r'%sstatic/(?P<path>.*)$' % settings.URL_PATH_BASE, 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	(r'^%s$' % settings.URL_PATH_BASE, include('home.urls')),
	(r'^%shome/' % settings.URL_PATH_BASE, include('home.urls')),
	(r'^%susers/' % settings.URL_PATH_BASE, include('users.urls')),
	(r'^%smails/' % settings.URL_PATH_BASE, include('mails.urls')),
	(r'^%sfw/' % settings.URL_PATH_BASE, include('fw.urls')),
	(r'^%s__admin/(.*)' % settings.URL_PATH_BASE, admin.site.root),
)
