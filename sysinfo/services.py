# -*- coding: utf-8 -*-

import os
import datetime, time
from re import compile,IGNORECASE

from sysinfo.config import SERVICES, CONFIG

MINUTE  = 60
HOUR    = MINUTE * 60
DAY     = HOUR * 24

class init:

	__services={}

	def __init__(self):
		self.__services=SERVICES
		self.__get_pids()
		self.__make_service_uptime()

	def get_services(self):
		return self.__services
	
	def __get_pids(self):
		
		for service in self.__services.keys():
			try:
				pidfile = open(SERVICES[service]['pidfile'],'r')
				self.__services[service]['pid'] = int(pidfile.readline()) #.replace('\n','')
				self.__services[service]['is_running'] = self.__pid_exists(self.__services[service]['pid'])
				pidfile.close()
			except IOError:
				self.__services[service]['is_running'] = False

	def __make_service_uptime(self):

	
		for service in self.__services.keys():
			try:
				t = os.stat(self.__services[service]['pidfile']).st_mtime
				now = time.mktime(datetime.datetime.now().timetuple())

				diff = now - t

				if diff < 60.0:
					self.__services[service]['uptime'] = "%is" %diff
				else:
					for i in ((60,'m'), (60,'h'),(24,'d')):
						if diff > i[0]:
							diff = diff / i[0]
							self.__services[service]['uptime'] = "%.2f%s" %(diff,i[1])

			except OSError:
				self.__services[service]['is_running'] = False
				self.__services[service]['uptime'] = False

	def __pid_exists(self,pid):

		try:
			os.kill(pid, 0)
			return True
		except OSError, err:
			#return err.errno
			return False
	
	def service_command(self, service, cmd):

		try:
			service_command=self.__services[service][cmd]
		except KeyError:
			return (False,'No hay un comando para ejecutar')

		if service_command:

			import subprocess

			try:
				ret = subprocess.Popen(service_command+" "+cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

				salida=ret.communicate()
			except OSError, e:
				return (False,e[1])

#Solo una prueba, fallida por cierto.
#			try:
#				sts = os.waitpid(ret.pid, 0)
#			except OSError, e:
#				pass

			if not ret.returncode == 0:
				return (False,salida[1])

			self.__get_pids()
			self.__make_service_uptime()
			return (True,salida[0])
			
		return (False,'La variable esta vacía')
