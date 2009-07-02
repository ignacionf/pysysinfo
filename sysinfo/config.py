# -*- coding: utf-8 -*-

DISTROS = [
	{'name': 'Debian','files': ('/etc/debian_release','/etc/debian_version',)},
	{'name': 'SUSE LINUX','files': ('/etc/SuSE-release','/etc/UnitedLinux-release',)},
	{'name': 'Mandrage','files': ('/etc/mandrake-release',)},
	{'name': 'MandrivaLinux','files': ('/etc/mandrake-release',)},
	{'name': 'Gentoo','files': ('/etc/gentoo-release',)},
	{'name': 'Fedora','files': ('/etc/fedora-release',)},
	{'name': 'FedoraCore','files': ('/etc/fedora-release',)},
	{'name': 'RedHat','files': ('/etc/redhat-release','/etc/redhat_version',)},
	{'name': 'Slackware','files': ('/etc/slackware-release','/etc/slackware-version',)},
	{'name': 'Trustix','files': ('/etc/trustix-release','/etc/trustix-version',)},
	{'name': 'FreeEOS','files': ('/etc/eos-version',)},
	{'name': 'Arch','files': ('/etc/arch-release',)},
	{'name': 'Cobalt','files': ('/etc/cobalt-release',)},
	{'name': 'LinuxFromScratch','files': ('/etc/lfs-release',)},
	{'name': 'Rubix','files': (' /etc/rubix-version',)},
	{'name': 'Ubuntu','files': ('/etc/lsb-release',)},
	{'name': 'PLD','files': ('/etc/pld-release',)},
	{'name': 'CentOS','files': ('/etc/redhat-release','/etc/redhat_version',)},
	{'name': 'RedHatEnterpriseES','files': ('/etc/redhat-release','/etc/redhat_version',)},
	{'name': 'RedHatEnterpriseAS','files': ('/etc/redhat-release','/etc/redhat_version',)},
	{'name': 'LFS','files': ('/etc/lfs-release','/etc/lfs_version',)},
	{'name': 'HLFS','files': ('/etc/hlfs-release','/etc/hlfs_version',)},
	{'name': 'IYCC','files': ('/etc/lsb-release',)},
	{'name': 'Synology','files': ('/etc/synoinfo.conf',)},
]

FILES = {
	'kernel_version': '/proc/version',
	'uptime': '/proc/uptime',
	'loadavg': '/proc/loadavg',
	'cpuavg': '/proc/stat',
	'meminfo': '/proc/meminfo',
	'cpuinfo': '/proc/cpuinfo',
	}
