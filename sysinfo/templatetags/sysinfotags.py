# -*- coding: utf-8 -*-

from django.template import Library, Node, resolve_variable, VariableDoesNotExist, TemplateSyntaxError 
from django.template.loader import get_template
from django.template import Context

from django.conf import settings

import datetime, calendar

register = Library()

@register.filter(name='progress')
def progress(level):

	level=int(level)

	if level > settings.SYSINFO_PROGRESSBAR['max']:
		border="#CA1414"
		background="#DC243C"
	elif level > settings.SYSINFO_PROGRESSBAR['alert']:
		border="#FC9D9A"
		background="#F9CDAD"
	else:
		border="#83BF4D"
		background="#96D57C"
	
	html="<div class='ui-corner-all' style='width: 100px; border: 1px solid %s; height: 16px;'>" % border
	html+="<div style='color: black;height: 16px; width: %ipx; background-color: %s;'>%i&#37;</div>" % (level,background,level)
	html+="</div>"

	return html
