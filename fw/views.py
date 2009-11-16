# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson
from django.http import HttpResponseRedirect, HttpResponse

# Users 
from django.contrib.auth.decorators import login_required

from pysysinfo.libs.utils import *

from fw.models import *
from fw.forms import *

@login_required
def index(response, template_name):
	o={'data': Zone.objects.all().order_by('name'), 'module_url': 'fw'} 
	return render_to_response(template_name, o, context_instance=RequestContext(response))

@login_required
def addZone(response, template_name):
	Form=ZoneForm
	url="%s/fw/" %settings.URL_PATH_BASE
	o={'form': Form(),'title': "Nueva Zona de Firewall", 'module_url': 'fw'}

	if response.method == 'POST':
		o['form'] = Form(response.POST)

		if o['form'].is_valid():
			try:
				o['form'].save()
				return HttpResponseRedirect(url)
			except:
				o['errors']=get_error("addZone Error: no se pudo crear la zona")

	return render_to_response(template_name, o, context_instance=RequestContext(response))

@login_required
def editZone(response, template_name, id):

	Form=ZoneForm
	url="%s/fw/" %settings.URL_PATH_BASE
	o={}

	try:
		data=Zone.objects.get(pk=int(id))
	except:
		return HttpResponseRedirect("%s/fw/" %settings.URL_PATH_BASE)

	if response.method == 'POST':

		o['form'] = Form(response.POST, instance=data)

		if o['form'].is_valid():

			try:
				o['form'].save()
				return HttpResponseRedirect(url)
			except:
				o['errors']=get_error("editZone Error: no se pudo actualizar la zona")
	else:
		o['form']= Form(instance=data)
	
	o['title']="Editar zona %s" % data

	return render_to_response(template_name, o, context_instance=RequestContext(response))

@login_required
def deleteZone(response, id):
	
	try:
		Zone.objects.get(pk=int(id)).delete()
	except:
		pass
	return HttpResponseRedirect("%s/fw/" %settings.URL_PATH_BASE)

######################################3
### Rules

@login_required
def rules(response, template_name):
	o={'data': Rule.objects.all().order_by('name'), 'module_url': 'fw/rules'} 
	return render_to_response(template_name, o, context_instance=RequestContext(response))

@login_required
def addRule(response, template_name):
	Form=RuleForm
	url="%s/fw/rules/" %settings.URL_PATH_BASE
	o={'form': Form(),'title': "Nueva Regla de Firewall", 'module_url': 'fw/rules'}

	if response.method == 'POST':
		o['form'] = Form(response.POST)

		if o['form'].is_valid():
			try:
				o['form'].save()
				return HttpResponseRedirect(url)
			except:
				o['errors']=get_error("addRule Error: no se pudo crear la regla")

	return render_to_response(template_name, o, context_instance=RequestContext(response))

@login_required
def editZone(response, template_name, id):

	Form=ZoneForm
	url="%s/fw/" %settings.URL_PATH_BASE
	o={}

	try:
		data=Zone.objects.get(pk=int(id))
	except:
		return HttpResponseRedirect("%s/fw/" %settings.URL_PATH_BASE)

	if response.method == 'POST':

		o['form'] = Form(response.POST, instance=data)

		if o['form'].is_valid():

			try:
				o['form'].save()
				return HttpResponseRedirect(url)
			except:
				o['errors']=get_error("editZone Error: no se pudo actualizar la zona")
	else:
		o['form']= Form(instance=data)
	
	o['title']="Editar zona %s" % data

	return render_to_response(template_name, o, context_instance=RequestContext(response))

@login_required
def deleteZone(response, id):
	
	try:
		Zone.objects.get(pk=int(id)).delete()
	except:
		pass
	return HttpResponseRedirect("%s/fw/" %settings.URL_PATH_BASE)

######################################3
### Rules

