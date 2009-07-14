from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^$', 'home.views.index', {'template_name': 'index.html'}),
	(r'^index/$', 'home.views.index', {'template_name': 'index.html'}),
	(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
	(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}),
	(r'^info/disk/$', 'home.views.diskinfo', {'template_name': 'sysinfo/diskinfo.html'}),
	(r'^info/mem/$', 'home.views.meminfo', {'template_name': 'sysinfo/meminfo.html'}),
	(r'^info/sys/$', 'home.views.sysinfo', {'template_name': 'sysinfo/sysinfo.html'}),
	(r'^info/cpu/$', 'home.views.cpuinfo', {'template_name': 'sysinfo/cpuinfo.html'}),
	(r'^info/pci/$', 'home.views.pciinfo', {'template_name': 'sysinfo/pciinfo.html'}),
	(r'^info/iface/$', 'home.views.ifaceinfo', {'template_name': 'sysinfo/ifaceinfo.html'}),
	(r'^info/services/$', 'home.views.servicesinfo', {'template_name': 'sysinfo/servicesinfo.html'}),
	(r'^service/(?P<service>\S+)/$', 'home.views.service_cmd'),
)
