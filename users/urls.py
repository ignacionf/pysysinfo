from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^$', 'users.views.index', {'template_name': 'users/index.html'}),
	(r'^add/$', 'users.views.addUser', {'template_name': 'users/formUser.html'}),
	(r'^edit/(?P<id>\d+)/$', 'users.views.editUser', {'template_name': 'users/formUser.html'}),
	(r'^delete/(?P<id>\d+)/$', 'users.views.deleteUser'),

	(r'^groups/$', 'users.views.groups', {'template_name': 'users/groups.html'}),
	(r'^groups/add/$', 'users.views.addGroup', {'template_name': 'users/formGroup.html'}),
	(r'^groups/edit/(?P<id>\d+)/$', 'users.views.editGroup', {'template_name': 'users/formGroup.html'}),
	(r'^groups/delete/(?P<id>\d+)/$', 'users.views.deleteGroup'),

	(r'^relUserGroup/$', 'users.views.relUserGroup', {'template_name': 'users/relUserGroup.html'}),
	(r'^relUserGroup/add/$', 'users.views.addUserGroup', {'template_name': 'users/formRelacion.html'}),
	(r'^relUserGroup/delete/(?P<id>\d+)/$', 'users.views.deleteUserGroup'),
)
