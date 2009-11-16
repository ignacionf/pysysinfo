# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User

from users.models import *
from mails.models import MailVirtualDomain

class UserForm(forms.Form):
	""" Formulario para generar un usuario """

	name = forms.CharField(label='Nombre Completo', max_length=255, required=True)
	username = forms.CharField(label='Nombre de Usuario', max_length=255, required=True)
	password = forms.CharField(label='Contraseña',min_length = 6, widget = forms.PasswordInput,required=True)
	password_check = forms.CharField(label='Confirmación de Contraseña',min_length = 6, widget = forms.PasswordInput,required=True)
	gid = forms.ChoiceField(label='Grupo Principal', choices=[(x.gid, x.groupname) for x in Grupo.objects.all()])
	domain = forms.ChoiceField(label='Dominio de mail', choices=[(x.id, x.domain) for x in MailVirtualDomain.objects.all()])
	shell = forms.ChoiceField(label='Shell', choices=(('/bin/bash','Bash'),('/bin/false','False')))

	smtpaccess = forms.ChoiceField(label='Acceso SMTP', choices=(('1','Denegar'),('0','Aceptar')))
	pop3access = forms.ChoiceField(label='Acceso POP3', choices=(('1','Denegar'),('0','Aceptar')))
	imapaccess = forms.ChoiceField(label='Acceso IMAP', choices=(('1','Denegar'),('0','Aceptar')))
	webmailaccess = forms.ChoiceField(label='Acceso Webmail', choices=(('1','Denegar'),('0','Aceptar')))
	proxyaccess = forms.ChoiceField(label='Acceso Proxy', choices=(('1','Denegar'),('0','Aceptar')))
	ftpaccess = forms.ChoiceField(label='Acceso FTP', choices=(('1','Denegar'),('0','Aceptar')))

	def clean_password_check(self):
		if self.cleaned_data.get('password_check'):
			p = self.cleaned_data.get('password')
			p_c = self.cleaned_data.get('password_check')

			if p != p_c:
				raise forms.ValidationError('Los passwords no coinciden')
	
	def clean_username(self):
		if self.cleaned_data.get('username'):
			u = self.cleaned_data.get('username')

			try:
				user=User.objects.get(username=u)
				raise forms.ValidationError('El nombre de usuario "%s" ya se encuentra en uso.' % u)
			except User.DoesNotExist:
				return u
	
class EditUserForm(forms.Form):
	""" Formulario para editar un usuario """

	name = forms.CharField(label='Nombre Completo', max_length=255, required=True)
	password = forms.CharField(label='Contraseña',min_length = 6, widget = forms.PasswordInput,required=False)
	password_check = forms.CharField(label='Confirmación de Contraseña',min_length = 6, widget = forms.PasswordInput,required=False)
	gid = forms.ChoiceField(label='Grupo Principal', choices=[(x.gid, x.groupname) for x in Grupo.objects.all()])
	domain = forms.ChoiceField(label='Dominio de mail', choices=[(x.id, x.domain) for x in MailVirtualDomain.objects.all()])
	shell = forms.ChoiceField(label='Shell', choices=(('/bin/bash','Bash'),('/bin/false','False')))

	smtpaccess = forms.ChoiceField(label='Acceso SMTP', choices=(('1','Denegar'),('0','Aceptar')))
	pop3access = forms.ChoiceField(label='Acceso POP3', choices=(('1','Denegar'),('0','Aceptar')))
	imapaccess = forms.ChoiceField(label='Acceso IMAP', choices=(('1','Denegar'),('0','Aceptar')))
	webmailaccess = forms.ChoiceField(label='Acceso Webmail', choices=(('1','Denegar'),('0','Aceptar')))
	proxyaccess = forms.ChoiceField(label='Acceso Proxy', choices=(('1','Denegar'),('0','Aceptar')))
	ftpaccess = forms.ChoiceField(label='Acceso FTP', choices=(('1','Denegar'),('0','Aceptar')))

	def clean_password_check(self):
		if self.cleaned_data.get('password_check'):
			p = self.cleaned_data.get('password')
			p_c = self.cleaned_data.get('password_check')

			if p != p_c:
				raise forms.ValidationError('Los passwords no coinciden')
	
	def clean_username(self):
		if self.cleaned_data.get('username'):
			u = self.cleaned_data.get('username')

			try:
				user=User.objects.get(username=u)
				raise forms.ValidationError('El nombre de usuario "%s" ya se encuentra en uso.' % u)
			except User.DoesNotExist:
				return u
				
from django.forms import ModelForm
class GroupForm(ModelForm):
	class Meta:
		model = Grupo

class UserGroupForm(ModelForm):
	class Meta:
		model = AdminGrupos
