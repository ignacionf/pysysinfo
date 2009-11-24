from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^$', 'mails.views.index', {'template_name': 'mails/index.html'}),
	(r'^add/$', 'mails.views.addDomain', {'template_name': 'mails/formDomain.html'}),
	(r'^edit/(?P<id>\d+)/$', 'mails.views.editDomain', {'template_name': 'mails/formDomain.html'}),
	(r'^delete/(?P<id>\d+)/$', 'mails.views.deleteDomain'),

	(r'^alias/$', 'mails.views.alias', {'template_name': 'mails/alias.html'}),
	(r'^alias/add/$', 'mails.views.addAlias', {'template_name': 'mails/formAlias.html'}),
	(r'^alias/delete/(?P<id>\d+)/$', 'mails.views.deleteAlias'),

	(r'^mailq/$', 'mails.views.mailq', {'template_name': 'mails/mailq.html'}),
	(r'^config/$', 'mails.views.config', {'template_name': 'mails/config.html'}),
	(r'^log/$', 'mails.views.log', {'template_name': 'mails/logs.html'}),

)
