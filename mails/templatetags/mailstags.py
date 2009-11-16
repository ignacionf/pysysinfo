# -*- coding: utf-8 -*-

from django.template import Library, Node, resolve_variable, VariableDoesNotExist, TemplateSyntaxError 
from django.template.loader import get_template
from django.template import Context

from django.conf import settings

import datetime, calendar

register = Library()

@register.filter(name='truncate')
def truncate(text, length):

	if len(text) > length+3:
		new_text = text[0:length]+"..."
	else:
		new_text = text

	return new_text

@register.filter(name='mailerror')
def mailerror(text, paso):
	
	new_text=""
	for i in range(0,len(text),paso):
		new_text+=text[i:i+paso]+"<br />"
	return new_text
