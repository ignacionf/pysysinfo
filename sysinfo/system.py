# -*- coding: utf-8 -*-

import os
from re import compile
from socket import getfqdn, gethostname

from sysinfo.config import FILES, DISTROS

MINUTE  = 60
HOUR    = MINUTE * 60
DAY     = HOUR * 24

class init:

	def __init__(self):
		pass
	
	def version(self):
		try:
			self.__version=open(FILES['kernel_version'],'r').read()
			return self.__version_parse(self.__version)
		except IOError:
			return None

		# Otra opcion es:
		#files=('osrelease','ostype','version')
		#r={}
		#for i in files:
		#	r[i]=open('/proc/sys/kernel/%s' % i,'r').readline()

		#return r
			
	
	def __version_parse(self,line):
		com=compile(r"(\S+) version (\S+) \((.*)\) \((.*) \((.*)\) #(\d+) (\S+) (.*)")
		g=com.match(line).groups()

		r={'systype': g[0], 'version': g[1], 'compile_number': g[5], 'MP': g[6],
			'compile_date': g[7], 'compile_author': g[3][:-1], 'compile_system': g[2],
			'compile_base': g[4] }
		return r
	
	def getFQDN(self):
		return getfqdn()
	
	def getHostName(self):
		return gethostname()
	
	def getArch(self):
		for distro in DISTROS:
			for file in distro['files']:
				try:
					return distro['name'],open(file,'r').read()
				except IOError:
					pass
	
	def uptime(self):
		try:
			f = open(FILES['uptime'])
			contents = f.read().split()
			f.close()
		except:
			return None

		total_seconds = float(contents[0])

		days    = int( total_seconds / DAY )
		hours   = int( ( total_seconds % DAY ) / HOUR )
		minutes = int( ( total_seconds % HOUR ) / MINUTE )
		seconds =  total_seconds

		return {'days': days, 'hours': hours, 'minutes': minutes, 'seconds': seconds }
	
	def loadavg(self):

		try:
			f = open(FILES['loadavg'])
			contents = f.read().split()
			f.close()
		except IOError:
			return None

		return {'EXT_1': float(contents[0]), 'EXT_5': float(contents[1]), 'EXT_15': float(contents[2])}
	
	def cpuavg(self):
		
		from time import sleep

		load=[]
		total=[]

		for i in (0,1):
			try:
				f = open(FILES['cpuavg'])
				contents = f.readline().split()
				f.close()
			except IOError:
				return None

			load.append(int(contents[1]) + int(contents[2]) + int(contents[3]) )
			total.append(int(contents[1]) + int(contents[2]) + int(contents[3])  + int(contents[4]))
			sleep(1)


		avg = (100 * (load[1]-load[0]) ) / ( total[1] - total[0] )

		return avg

	def meminfo(self):

		fields = ('MemTotal','MemFree','Buffers','Cached','SwapTotal','SwapFree')

		try:
			f = open(FILES['meminfo'])
			contents = {}
			for i in f.readlines():
				list = [compile("%s:\s+(\d+) kB" % x).match(i) for x in fields]

				if any(list):
					match = filter(None,list)[0]
					index=list.index(match)
					contents[fields[index].lower()]=int(match.groups()[0])/1024
			f.close()
		except IOError:
			return None

		contents['memused']=contents['memtotal']-contents['memfree']
		contents['memavg']=(contents['memused'] * 100)/contents['memtotal']

		contents['memcachedavg']=(contents['cached'] * 100)/contents['memtotal']
		contents['membuffersavg']=(contents['buffers'] * 100)/contents['memtotal']

		contents['swapused']=contents['swaptotal']-contents['swapfree']
		try:
			contents['swapavg']=(contents['swapused'] * 100)/contents['swaptotal']
		except ZeroDivisionError:
			contents['swapavg']=0

		return contents
