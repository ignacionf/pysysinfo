# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson
from django.http import HttpResponseRedirect, HttpResponse

# Users 
from django.contrib.auth.decorators import login_required

from pysysinfo.libs.utils import *

from users.models import *
from mails.models import *

from mails.forms import *

@login_required
def index(response, template_name):
	o={'data': MailVirtualDomain.objects.all().order_by('domain') } 
	return render_to_response(template_name, o, context_instance=RequestContext(response))

@login_required
def alias(response, template_name):
	o={'data': AliasMail.objects.all().order_by('alias') } 
	return render_to_response(template_name, o, context_instance=RequestContext(response))

@login_required
def addDomain(response, template_name):
	o={'form': DomainForm()}

	if response.method == 'POST':
		o['form'] = DomainForm(response.POST)

		if o['form'].is_valid():
			try:
				o['form'].save()
				return HttpResponseRedirect("%s/mails/" %settings.URL_PATH_BASE)
			except:
				o['errors']=get_error("addDomain Error: no se pudo crear el dominio")

	return render_to_response(template_name, o, context_instance=RequestContext(response))

@login_required
def editDomain(response, template_name, id):

	o={}

	try:
		data=MailVirtualDomain.objects.get(pk=int(id))
	except:
		return HttpResponseRedirect("%s/mails/" %settings.URL_PATH_BASE)

	if response.method == 'POST':

		o['form'] = DomainForm(response.POST, instance=data)

		if o['form'].is_valid():

			try:
				o['form'].save()
				return HttpResponseRedirect("%s/mails/" %settings.URL_PATH_BASE)
			except:
				o['errors']=get_error("editDomain Error: no se pudo actualizar el dominio")
	else:
		o['form']= DomainForm(instance=data)
	
	o['title']="Editar Dominio %s" % data.domain

	return render_to_response(template_name, o, context_instance=RequestContext(response))

@login_required
def deleteDomain(response, id):
	
	try:
		MailVirtualDomain.objects.get(pk=int(id)).delete()
	except:
		pass
	return HttpResponseRedirect("%s/mails/" %settings.URL_PATH_BASE)

######################################3
### Alias

@login_required
def addAlias(response, template_name):
	o={'form': AliasForm()}

	if response.method == 'POST':
		o['form'] = AliasForm(response.POST)

		if o['form'].is_valid():

			alias = AliasMail(alias=response.POST['alias'], destination=Usuario.objects.get(pk=int(response.POST['destination'])))
			try:
				alias.save()
				return HttpResponseRedirect("%s/mails/alias/" %settings.URL_PATH_BASE)
			except:
				o['errors']=get_error("addAlias Error: no se pudo crear el dominio")

	return render_to_response(template_name, o, context_instance=RequestContext(response))

@login_required
def deleteAlias(response, id):
	
	try:
		AliasMail.objects.get(pk=int(id)).delete()
	except:
		pass
	return HttpResponseRedirect("%s/mails/alias/" %settings.URL_PATH_BASE)

######################################3
### Mailq 

from sysinfo.mails import Mailq

@login_required
def mailq(response, template_name):
	o={'data': Mailq().parse()}

	return render_to_response(template_name, o, context_instance=RequestContext(response))

######################################
### Config

from random import choice
import string

@login_required
def config(response, template_name):
	o={'muser': getRandomChar(), 'mpass': getRandomChar(), 'db': settings.DATABASE_NAME, 'home': settings.HOMEDIR}

	return render_to_response(template_name, o, context_instance=RequestContext(response))

def getRandomChar(l=10):
	chars = string.letters + string.digits
	r=''
	for i in range(0, l):
		r+=choice(chars)
	
	return r

######################################
### logs

from sysinfo import logs

@login_required
def log(response, template_name):
	o={'logs': logs.init().mail()}

	return render_to_response(template_name, o, context_instance=RequestContext(response))


