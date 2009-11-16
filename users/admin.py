from django.contrib import admin
from users.models import *

class UsuarioAdmin(admin.ModelAdmin):
	list_display = ('username','name','domain')
	list_filter = ('domain','username')
	ordering = ('username','name','domain')
	search_fields = ['username']
	fieldsets = (
		("Datos Personales", {'fields':('name','username')}),
		("Password", {'fields':('clear',)}),
		("Datos del sistema", {'fields':('domain','uid','gid','homedir','maildir', 'quota','shell')}),
		("Restricciones", {'fields':('smtpaccess','pop3access','imapaccess','webmailaccess',
			'proxyaccess','phpbbaccess','ftpaccess')}),
	)

admin.site.register(Usuario, UsuarioAdmin)

class GrupoAdmin(admin.ModelAdmin):
	list_display = ('groupname','groupdesc','gid')
	ordering = ('groupname','gid')
	search_fields = ['groupname']
admin.site.register(Grupo, GrupoAdmin)

class AdminGruposAdmin(admin.ModelAdmin):
	list_display = ('uid','gid')
	ordering = ('gid','uid')
	search_fields = ['uid']
admin.site.register(AdminGrupos,AdminGruposAdmin)
