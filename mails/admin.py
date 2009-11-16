from django.contrib import admin
from mails.models import *

admin.site.register(MailVirtualDomain)

class AliasMailAdmin(admin.ModelAdmin):
	fieldsets = ( ("Alias de Mail", {'fields': ('alias','destination',)} ), )
admin.site.register(AliasMail, AliasMailAdmin)
