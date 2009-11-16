from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^$', 'fw.views.index', {'template_name': 'fw/index.html'}),
	(r'^add/$', 'fw.views.addZone', {'template_name': 'fw/formZone.html'}),
	(r'^edit/(?P<id>\d+)/$', 'fw.views.editZone', {'template_name': 'fw/formZone.html'}),
	(r'^delete/(?P<id>\d+)/$', 'fw.views.deleteZone'),

	(r'^rules/$', 'fw.views.rules', {'template_name': 'fw/rules.html'}),
	(r'^rules/add/$', 'fw.views.addRule', {'template_name': 'fw/formRule.html'}),
	(r'^rules/edit/(?P<id>\d+)/$', 'fw.views.editRule', {'template_name': 'fw/formRule.html'}),
	(r'^rules/delete/(?P<id>\d+)/$', 'fw.views.deleteRule'),


)
