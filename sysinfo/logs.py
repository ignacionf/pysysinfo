# -*- coding: utf-8 -*-

from re import compile
from datetime import datetime
import time

from sysinfo.config import FILES

class init:

	def __init__(self):
		self.__logMail=[]
	
	def mail(self):
		
		match = compile("^(?P<mon>\S+) (?P<day>\d+) (?P<time>\S+) (?P<hostname>\S+) postfix/(?P<daemon>\S+)\[(?P<pid>\d+)\]: (?P<info>.*)$")

		info_matchs=(compile("^(?P<status>warning|fatal): (?P<msg>.*)$"), compile("^(?P<mail_id>[0-9A-F]*): (?P<msg>.*)$"), compile("^(?P<msg>.*)$"))
		msg_matchs = (compile("(?P<field>\S+)=(?P<value>\S+)"),compile("\((?P<msg>.*)\)"))

		for line in open(FILES['maillog'],'r').readlines():
			m = match.match(line.strip())
			if m:
				list = [x.match(m.group("info").strip()) for x in info_matchs]
				if any(list):
					info=filter(None,list)[0].groupdict()
					info['original']=info['msg']

					msg = {}
					for i in msg_matchs[0].findall(info['msg'].replace(',','')):
						if i[0] != '' and i[0] != "'":
							msg[i[0]]=i[1]

					if msg != {}:
						info['data']=msg

						msg = msg_matchs[1].search(info['msg'])
						if msg:
							info['msg']=msg.group('msg')
						else:
							info['msg']=''

				self.__logMail.append({'date': datetime.fromtimestamp(time.mktime(
						time.strptime("%s %s %s %s" % (m.group("day"), m.group("mon"), time.gmtime().tm_year, m.group("time")), "%d %b %Y %H:%M:%S"))),
						'hostname': m.group("hostname"),
						'daemon': m.group("daemon"),
						'pid': m.group("pid"),
						'info': info})

		return self.__logMail


if __name__ == "__main__":
	i = init()
	i.mail()
