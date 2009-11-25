# -*- coding: utf-8 -*-

from django.template import Library, Node, resolve_variable, VariableDoesNotExist, TemplateSyntaxError 
from django.template.loader import get_template
from django.template import Context

from random import choice
import string

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

@register.filter(name='truncatelog')
def truncatelog(text, l):
	
	chars = string.letters + string.digits
	r=''
	for i in range(0, 10):
		r+=choice(chars)

	if len(text) > l+6:
		new_text = text[0:l]+"... <a href='#' class='logmore' id='%s'>[+]</a><div id='div_%s' class='moreinfo ui-corner-all'>%s</div>" % (r,r,text)
	else:
		new_text = text

	return new_text
