# -*- coding: utf-8 -*-
from django.conf import settings

if settings.DEBUG:
	import sys

	def get_error(msg=None):
		return "Mensaje de error: %s" % str(sys.exc_info())
else:
	def get_error(msg=None):
		if msg:
			return msg
		else:
			return "Error Desconocido"


class InputData:

	error = False
	data = {}
	
	def __init__(self,form):

		self.form = form
		
		if self.form.is_valid():
			self.data = form.cleaned_data
		else:
			self.error = True
	
	def errors(self):
		
		error_list = ""

		for key in self.form.errors.keys():
			msg_error="%s" % self.form.errors[key].as_text()[2:]
			label_error=self.form[key].label
			error_list += "<li><span style='display: none;'>%s</span><b>%s:</b> %s</li>\n" % (msg_error,label_error,msg_error)

		return error_list
	
	def get_clean(self,key):
		return self.data[key]
	
	def save(self):
		self.form.save()


