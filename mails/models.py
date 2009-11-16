# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
class MailVirtualDomain(models.Model):
	domain = models.CharField('Dominio',max_length=200, unique=True)
	destination = models.CharField('Destino',max_length=200,default="maildrop:")
	def __str__(self):
		return self.domain
	
	def get_num_of_users(self):
		from users.models import Usuario
		return len(Usuario.objects.all().filter(domain=self))

	class Meta:
		verbose_name = "Administracion de Dominio"
	
from users.models import Usuario
class AliasMail(models.Model):
	alias = models.CharField('Alias de Mail',max_length=200, unique=True)
	destination = models.ForeignKey(Usuario)

	def __str__(self):
		return self.alias
	class Meta:
		verbose_name = "Administracion de Alias de Mail"
