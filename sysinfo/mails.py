#!/usr/bin/env python

import os
import sys
import re
import time
import datetime

class MailInfo:

	mid = ""
	size = 0
	sender = ""
	datetime = ""
	recipients = []
	error = ""

	def __init__(self,mid, size=0, sender="", _datetime= "", recipients=[], error=""):
		self.mid = mid
		self.setSize(size)
		self.setSender(sender)
		self.setDatetime(_datetime)
		self.recipients = []
		self.setRecipients(recipients)
		self.setError(error)
	
	def setSize(self, size):
		if size != 0:
			self.size=size
	
	def setSender(self, sender):
		if sender != "":
			self.sender = sender
	
	def setDatetime(self, data):
		if data != "":
			self.datetime = datetime.datetime.fromtimestamp(time.mktime(time.strptime(data+" %s" % time.gmtime().tm_year, "%a %b %d %H:%M:%S %Y")))
	
	def setRecipients(self, recipients):
		if recipients != []:
			self.recipients.append(recipients)
	def setError(self, error):
		if error != "":
			self.error=error
	
	def __str__(self):
		return "id=%s, size=%s, sender=%s, datetime=%s, recipients=%s, error=%s" %(self.mid, self.size, self.sender, self.datetime, self.recipients, self.error)

class Mailq:

	def __init__(self):
		pass
	
	def parse(self):
		hre = re.compile('.*Queue ID.*')
		idre = re.compile(r"""
			^(?P<id>[0-9A-Z\*]+)
			\s+(?P<size>[0-9]+)
			\s+(?P<dow>\S+)
			\s+(?P<mon>\S+)
			\s+(?P<day>[0-9]+)
			\s+(?P<time>\S+)
			\s+(?P<sender>\S+)
			""", re.VERBOSE)
		reasonre = re.compile('^\s*\(')
		recre = re.compile('^\s+(?P<recip>[^@]+@[^@]+)')
		sepre = re.compile('^$')

		salida = []

		mq = os.popen("/usr/bin/mailq", "r")
		for line in mq.readlines():

			line = line.rstrip()
			if hre.search(line): continue

			mo = idre.match(line)
			if mo:
				r = MailInfo(mo.group('id'),size=int(mo.group('size')),
					_datetime=' '.join((mo.group('dow'), mo.group('mon'), mo.group('day'), mo.group('time'))),
					sender=mo.group('sender'))
			else:
				mo = reasonre.match(line)
				if mo:
					r.setError(line.strip())
				else:
					mo = recre.match(line)
					if mo:
						r.setRecipients(mo.group('recip'))
					else:
						mo = sepre.match(line)
						if mo:
							salida.append(r)
	        mq.close()
	        return salida
