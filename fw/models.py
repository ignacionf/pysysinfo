# -*- coding: utf-8 -*-

from django.db import models

class Zone(models.Model):
	name = models.CharField('Nombre de la Zona',max_length=64, unique=True)
	description = models.CharField('Descripción de la Zona',max_length=255)

	def __str__(self):
		return self.name
	
	class Meta:
		verbose_name = "Zonas del Firewall"

CHAINS=[('INPUT','Chain:Entrada'), ('OUTPUT','Chain:Salida'), ('FORWARD','Chain:Forward')]

[CHAINS.append((x.name,"Zona:%s" % x.name)) for x in Zone.objects.all()]

PROTO=(("all","Todos"), ("tcp","TCP"), ("udp","UDP"), ("icmp","ICMP"))

def getPorts():
	import re

	pattern = re.compile("(?P<service>\S+)\s+(?P<port>\d+)/(?P<proto>tcp|udp)")

	services=[]
	for line in open('/etc/services','r').readlines():
		m = pattern.match(line)
		if m:
			services.append((m.group('port'),"%s:%s (%s)" %(m.group('proto'),m.group('service'),m.group('port'))))
	
	return services

SERVICES=getPorts()
	
class Rule(models.Model):
	name = models.CharField('Nombre de la regla',max_length=64, unique=True)

	zone = models.ForeignKey(Zone,verbose_name='Pertenece a la Zona', blank=True, null=True)
	chain = models.CharField('Acción/Dirigir a Zona', max_length=16, choices=CHAINS)

	proto = models.CharField('Protocolo', max_length=4, choices=PROTO, default="all")

	src = models.IPAddressField("IP Origen", blank=True, null=True)
	dst = models.IPAddressField("IP Destino", blank=True, null=True)
	src_port = models.IntegerField("Puerto Origen", blank=True, null=True,choices=SERVICES)
	dst_port = models.IntegerField("Puerto Destino", blank=True, null=True,choices=SERVICES)

	def __str__(self):
		return self.name
	class Meta:
		verbose_name = "Reglas de Firewall"
