# -*- coding: utf-8 -*-

from django.db import models
import os

from mails.models import *

class Grupo(models.Model):
	groupname = models.CharField('Nombre del Grupo',max_length=200, unique=True)
	groupdesc = models.CharField('Descripcion del Grupo',max_length=200,default="[Descripción del grupo]")
	gid = models.IntegerField('Identificador de Grupo',default=99)

	def __str__(self):
		return self.groupname

	def getMaxGID(self):
		from django.db import connection
		cursor = connection.cursor()
		cursor.execute("select MAX(gid) as maxgid from users_grupo")
		row = cursor.fetchone()
		return row[0]

	def save(self):

		try:
			if self.gid == 99:
				self.gid=self.getMaxGID()+1
		except TypeError:
			self.gid=1001

		super(Grupo, self).save()
	
	class Meta:
		verbose_name = "Administracion de Grupo"

	
class Usuario(models.Model):
	username = models.CharField('Nombre del Usuario',max_length=200, unique=True)
	clear = models.CharField('Password',max_length=200)
	name = models.CharField('Nombre Completo',max_length=200)
	uid = models.IntegerField('Identificador de Usuario',default=100, unique=True)
	gid = models.IntegerField(default=99, verbose_name="Identificador de grupo")
	homedir = models.CharField('Directorio HOME',max_length=200,default='[auto gen]')
	maildir = models.CharField('Directorio de Mail',max_length=200,default='Maildir/')
	quota = models.CharField('Espacio disponible para Mails',max_length=200, default=0)
	shell = models.CharField('Shell',max_length=20, choices=(('/bin/bash','Bash'),('/bin/false','False')), default='/bin/false')
	domain = models.ForeignKey(MailVirtualDomain,verbose_name='Dominio al que pertenece')

	# Accesos
	smtpaccess = models.CharField("Acceso SMTP",max_length=1, choices=(('0','Accept'),('1','Deny')), default='0' )
	pop3access = models.CharField('Acceso POP3',max_length=1, choices=(('0','Accept'),('1','Deny')), default='0' )
	imapaccess = models.CharField('Acceso IMAP',max_length=1, choices=(('0','Accept'),('1','Deny')), default='0' )
	webmailaccess = models.CharField('Acceso al Webmail',max_length=1, choices=(('0','Accept'),('1','Deny')), default='0' )
	proxyaccess = models.CharField('Acceso al Proxy',max_length=1, choices=(('0','Accept'),('1','Deny')), default='0' )
	phpbbaccess = models.CharField('Acceso al Foro',max_length=1, choices=(('0','Accept'),('1','Deny')), default='0' )
	ftpaccess = models.CharField('Acceso al FTP',max_length=1, choices=(('0','Accept'),('1','Deny')), default='0' )

	def __str__(self):
		return self.username
	
	def getMaxUID(self):
		from django.db import connection
		cursor = connection.cursor()
		cursor.execute("select MAX(uid) as maxuid from users_usuario")
		row = cursor.fetchone()
		return row[0]
	
	def save(self):

		if self.homedir == '[auto gen]':
			self.homedir="/home/"+self.username

		try:
			if self.uid == 100:
				self.uid=self.getMaxUID()+1
		except TypeError:
			self.uid=1001

		super(Usuario, self).save()
		os.system('sudo /usr/local/sbin/makeHome %s' % self.username)
	
	def delete(self):
		super(Usuario,self).delete()
		os.system('sudo /usr/local/sbin/makeHome -r %s' % self.username)

	class Meta:
		verbose_name = "Administracion de Usuario"

class AdminGrupos(models.Model):
	uid =  models.ForeignKey(Usuario,related_name="Usuario")
	gid =  models.ForeignKey(Grupo,related_name="Grupo")

	def save(self):
		super(AdminGrupos, self).save()
		os.system('sudo /usr/local/sbin/mantenerGrupos.sh') 

	def delete(self):
		super(AdminGrupos, self).delete()
		os.system('sudo /usr/local/sbin/mantenerGrupos.sh') 

	class Meta:
		unique_together = (("uid", "gid"),)
		verbose_name = "Administracion de Usuarios:Grupo"
