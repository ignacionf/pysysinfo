# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User

from mails.models import *
from django.forms import ModelForm

class DomainForm(ModelForm):
	class Meta:
		model = MailVirtualDomain

class AliasForm(ModelForm):
	destination = forms.ChoiceField(label='Destino del mail', choices=[(x.id, "%s@%s" %(x.username,x.domain)) for x in Usuario.objects.all().order_by('domain','username')])
	class Meta:
		model = AliasMail
