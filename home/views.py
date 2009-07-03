# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext

# Users 
from django.contrib.auth.decorators import login_required

from sysinfo import system, hardware

@login_required
def index(response, template_name):
	o={}
	return render_to_response(template_name, o, context_instance=RequestContext(response))

@login_required
def diskinfo(response, template_name):
	hard=hardware.init()

	o={'info': hard.diskinfo()}
	return render_to_response(template_name, o, context_instance=RequestContext(response))

@login_required
def meminfo(response, template_name):
	OS=system.init()
	o={'meminfo': OS.meminfo() }
	return render_to_response(template_name, o, context_instance=RequestContext(response))

@login_required
def sysinfo(response, template_name):
	OS=system.init()
	sysinfo={'kernel': OS.version(), 'fqdn': OS.getFQDN(), 'distro': OS.getArch(), 'uptime': OS.uptime(),
		'loadavg': OS.loadavg(), 'cpuavg': OS.cpuavg() }
	o={'sysinfo': sysinfo}
	return render_to_response(template_name, o, context_instance=RequestContext(response))

@login_required
def cpuinfo(response, template_name):
	hard=hardware.init()
	o={'info': hard.cpuinfo()}
	return render_to_response(template_name, o, context_instance=RequestContext(response))

@login_required
def pciinfo(response, template_name):
	hard=hardware.init()
	o={'info': hard.lspci()}
	return render_to_response(template_name, o, context_instance=RequestContext(response))

@login_required
def ifaceinfo(response, template_name):
	hard=hardware.init()
	o={'info': hard.ifaceinfo()}
	return render_to_response(template_name, o, context_instance=RequestContext(response))
