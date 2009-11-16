# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson
from django.http import HttpResponseRedirect, HttpResponse

# Users 
from django.contrib.auth.decorators import login_required

from pysysinfo.libs.utils import *

from mails.models import *
from users.models import *
from users.forms import *

@login_required
def index(response, template_name):
	o={'usuarios': Usuario.objects.all().order_by('domain', 'username') } 
	return render_to_response(template_name, o, context_instance=RequestContext(response))

@login_required
def groups(response, template_name):
	o={'grupos': Grupo.objects.all().order_by('gid','groupname')}

	return render_to_response(template_name, o, context_instance=RequestContext(response))

@login_required
def relUserGroup(response, template_name):
	o={'relaciones': AdminGrupos.objects.select_related().order_by("users_usuario.username","users_grupo.groupname")}

	return render_to_response(template_name, o, context_instance=RequestContext(response))

@login_required
def addUser(response, template_name):
	o={'form': UserForm()}

	if response.method == 'POST':
		o['form'] = UserForm(response.POST)

		if o['form'].is_valid():
			data = o['form'].cleaned_data

			usuario = Usuario(username=data['username'], 
					clear=data['password'],
					gid=data['gid'],
					domain=MailVirtualDomain.objects.get(pk=data['domain']),
					shell=data['shell'],
					name=data['name'],
					phpbbaccess=u'0',
					webmailaccess=data['webmailaccess'],
					imapaccess=data['imapaccess'],
					pop3access=data['pop3access'],
					smtpaccess=data['smtpaccess'],
					ftpaccess=data['ftpaccess'],
					proxyaccess=data['proxyaccess'],
					maildir=u'Maildir/',
					homedir=u'[auto gen]',
					quota=u'0',
					)

			try:
				usuario.save()
				return HttpResponseRedirect("%s/users/" %settings.URL_PATH_BASE)
			except:
				o['errors']=get_error("addUser Error: no se pudo crear el usuario")

	return render_to_response(template_name, o, context_instance=RequestContext(response))

@login_required
def editUser(response, template_name, id):
	try:
		usuario=Usuario.objects.get(pk=int(id))
	except:
		return HttpResponseRedirect("%s/users/" %settings.URL_PATH_BASE)

	o={'title': "Editar Usuario %s" % usuario.username}

	if response.method == 'POST':
		o['form'] = EditUserForm(response.POST)

		if o['form'].is_valid():
			data = o['form'].cleaned_data

			if data['password'] != "":
				usuario.clear=data['password']
			usuario.gid=data['gid']
			usuario.domain=MailVirtualDomain.objects.get(pk=data['domain'])
			usuario.shell=data['shell']
			usuario.name=data['name']
			usuario.webmailaccess=data['webmailaccess']
			usuario.imapaccess=data['imapaccess']
			usuario.pop3access=data['pop3access']
			usuario.smtpaccess=data['smtpaccess']
			usuario.ftpaccess=data['ftpaccess']
			usuario.proxyaccess=data['proxyaccess']

			try:
				usuario.save()
				return HttpResponseRedirect("%s/users/" %settings.URL_PATH_BASE)
			except:
				o['errors']=get_error("addUser Error: no se pudo crear el usuario")
				o['caca']=data
	else:
		usuario_dict=usuario.__dict__
		usuario_dict['domain']=usuario.domain.id
		o['form']=EditUserForm(usuario_dict)

	return render_to_response(template_name, o, context_instance=RequestContext(response))

@login_required
def deleteUser(response, id):
	
	try:
		Usuario.objects.get(pk=int(id)).delete()
	except:
		pass
	return HttpResponseRedirect("%s/users/" %settings.URL_PATH_BASE)

#######################################
## Grupos

@login_required
def addGroup(response, template_name):
	o={'form': GroupForm()}

	if response.method == 'POST':
		o['form'] = GroupForm(response.POST)

		if o['form'].is_valid():

			try:
				group = o['form'].save()
				return HttpResponseRedirect("%s/users/groups/" %settings.URL_PATH_BASE)
			except:
				o['errors']=get_error("addGroup Error: no se pudo crear el usuario")

	return render_to_response(template_name, o, context_instance=RequestContext(response))


@login_required
def editGroup(response, template_name, id):

	o={}

	try:
		group=Grupo.objects.get(pk=int(id))
	except:
		return HttpResponseRedirect("%s/users/groups/" %settings.URL_PATH_BASE)

	if response.method == 'POST':

		o['form'] = GroupForm(response.POST, instance=group)

		if o['form'].is_valid():

			try:
				group = o['form'].save()
				return HttpResponseRedirect("%s/users/groups/" %settings.URL_PATH_BASE)
			except:
				o['errors']=get_error("addGroup Error: no se pudo crear el usuario")
	else:
		o['form']= GroupForm(instance=group)
	
	o['title']="Editar Grupo %s" % group.groupname


	return render_to_response(template_name, o, context_instance=RequestContext(response))

@login_required
def deleteGroup(response, id):
	
	try:
		Grupo.objects.get(pk=int(id)).delete()
	except:
		pass
	return HttpResponseRedirect("%s/users/groups/" %settings.URL_PATH_BASE)


#######################################
## Relación Usuairos y Grupos

@login_required
def addUserGroup(response, template_name):
	o={'form': UserGroupForm()}

	if response.method == 'POST':
		o['form'] = UserGroupForm(response.POST)

		if o['form'].is_valid():

			try:
				group = o['form'].save()
				return HttpResponseRedirect("%s/users/relUserGroup/" %settings.URL_PATH_BASE)
			except:
				o['errors']=get_error("addUserGroup Error: no se pudo crear el usuario")

	return render_to_response(template_name, o, context_instance=RequestContext(response))

@login_required
def deleteUserGroup(response, id):
	
	try:
		AdminGrupos.objects.get(pk=int(id)).delete()
	except:
		pass
	return HttpResponseRedirect("%s/users/relUserGroup/" %settings.URL_PATH_BASE)


