# -*- coding: utf-8 -*-

import os
from re import compile,IGNORECASE

from socket import getfqdn, gethostname

from sysinfo.config import FILES, DISTROS

MINUTE  = 60
HOUR    = MINUTE * 60
DAY     = HOUR * 24

class init:

	__pci_vendors={}
	__pci_devices={}
	__pci_subsys={}

	__pci_class={}
	__pci_subclass={}

	def __init__(self):
		pass
	
	def cpuinfo(self):

		fields = ("processor", "vendor_id", "cpu family", "model", "model name",
			"stepping", "cpu MHz", "cache size", "physical id",
			"siblings", "core id", "cpu cores", "apicid", "initial apicid",
			"fpu", "fpu_exception", "cpuid level", "wp", "flags", "bogomips",
			"clflush size", "cache_alignment", "address sizes", "power management")
		flags = ('apic','acpi','mmx',' sse2','ht','lm','vmx',' 3dnowext','3dnow')

		try:
			f = open(FILES['cpuinfo'])
			contents = {}
			for i in f.readlines():
				list = [compile("%s\s+:\s+(.*)" % x).match(i) for x in fields]

				if any(list):
					match = filter(None,list)[0]
					index=list.index(match)
					contents[fields[index].lower().replace(' ','_')]=match.groups()[0]
			f.close()
		except IOError:
			return None

		contents['processors']=(int(contents['processor'])+1)/int(contents['cpu_cores'])
		contents['cpu_speed']="%i Mhz" % float(contents['cpu_mhz'])

		aux=[]
		for i in contents['flags'].split():
			if i in flags:
				aux.append(i)

		contents['flags']=aux

		return contents

	def diskinfo(self):
		import subprocess

		output = subprocess.Popen(['/bin/df','-h' ],stdout=subprocess.PIPE).communicate()[0]
		lines = output.split('\n')[1:]

		disks=[]
		for line in lines:
			if not line: continue
			fs, blocks_total, blocks_used, blocks_available, used, mount = line.split()

			disks.append({'fs':fs, 'blocks_total':blocks_total,
				'blocks_used':blocks_used, 'blocks_available':blocks_available,
				'used': used[0:-1], 'mount': mount })

		return disks
	
	def lspci(self):
		
		self.__parse_pciids()

		PCI_DIR='/sys/bus/pci/devices/'
		pcis=[]
		for pci in os.listdir(PCI_DIR):
			dir='%s/%s' % (PCI_DIR,pci)

			vendor = self.get_vendor(open('%s/vendor' % dir ,'r').read()[2:-1])
			device = self.get_device(open('%s/device' % dir,'r').read()[2:-1])
			subsys_device = open('%s/subsystem_device' % dir,'r').read()[2:-1]
			subsys_vendor = open('%s/subsystem_vendor' % dir,'r').read()[2:-1]
			class_key = open('%s/class' % dir,'r').read()[2:-1]

			class_id=class_key[0:2]
			subclass_id=class_key[2:4]

			class_name=self.get_class(class_id)
			subclass_name=self.get_subclass(class_id, subclass_id)

			pcis.append({
				'bus': pci, 'dir': dir, 'vendor': vendor, 'device': device,
				'subsys_device': subsys_device, 'subsys_vendor': subsys_vendor,
				'class': class_name, 'subclass': subclass_name,
			})

			
		return pcis
	
	def __parse_pciids(self):
		PCIIDS='/usr/share/misc/pci.ids'

		matchs=(
			compile('^(?P<vendor>[0-9abcdef][0-9abcdef][0-9abcdef][0-9abcdef])\s+(?P<data>.*)$',IGNORECASE),
			compile('^\t(?P<device>[0-9abcdef][0-9abcdef][0-9abcdef][0-9abcdef])\s+(?P<data>.*)$',IGNORECASE),
			compile('^\t\t(?P<subvendor>[0-9abcdef][0-9abcdef][0-9abcdef][0-9abcdef])\s(?P<subdevice>[0-9abcdef][0-9abcdef][0-9abcdef][0-9abcdef])\s+(?P<data>.*)$',IGNORECASE),
			compile('^C\s(?P<class>[0-9abcdef][0-9abcdef])\s+(?P<data>.*)$',IGNORECASE),
			compile('^\t(?P<subclass>[0-9abcdef][0-9abcdef])\s+(?P<data>.*)$',IGNORECASE),
			)

		file = open(PCIIDS,'r')
		classid=''
		for line in file.readlines():
			list = [x.match(line) for x in matchs]
			if any(list):
				data = filter(None,list)[0]

				if 'vendor' in data.groupdict().keys():
					self.__pci_vendors[data.group('vendor')]=data.group('data')
				elif 'device' in data.groupdict().keys():
					self.__pci_devices[data.group('device')]=data.group('data')
				elif 'subvendor' in data.groupdict().keys():
					self.__pci_subsys["%s@%s" % (data.group('subvendor'),data.group('subdevice'))]=data.group('data')
				elif 'class' in data.groupdict().keys():
					classid=data.group('class')
					self.__pci_class[classid]=(data.group('data'),{})
				elif 'subclass' in data.groupdict().keys():
					self.__pci_class[classid][1][data.group('subclass')]=data.group('data')


		file.close()
	
	def get_vendor(self,vendor):
		try:
			return self.__pci_vendors[vendor]
		except KeyError:
			return vendor

	def get_device(self,device):
		try:
			return self.__pci_devices[device]
		except KeyError:
			return device

	def get_subsystem(self,subsys):
		try:
			return self.__pci_subsys[subsys]
		except KeyError:
			return subsys
	
	def get_class(self, class_id):
		try:
			return self.__pci_class[class_id][0]
		except KeyError:
			return class_id

	def get_subclass(self, class_id, subclass_id):
		try:
			return self.__pci_class[class_id][1][subclass_id]
		except KeyError:
			return subclass_id
