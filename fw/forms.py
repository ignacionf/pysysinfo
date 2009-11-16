# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User

from fw.models import *
from django.forms import ModelForm

class ZoneForm(ModelForm):
	class Meta:
		model = Zone

class RuleForm(ModelForm):
	class Meta:
		model = Rule
