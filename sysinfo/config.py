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
	'nicinfo': '/proc/net/dev',
	'maillog': '/var/log/mail.info',
	}

SERVICES={
	'Apache': {'pidfile': '/var/run/apache2.pid','start': '/usr/sbin/apache2ctl', 'stop': '/etc/init.d/apache2'}, # . /etc/apache2/envvars && echo $APACHE_PID_FILE
	'MySQL': {'pidfile': '/var/run/mysqld/mysqld.pid','start': '/etc/init.d/mysql', 'stop': '/etc/init.d/mysql'}, # /usr/sbin/mysqld --print-defaults | tr " " "\n" | grep pid-file | cut -d"=" -f2
	'SSH': {'pidfile': '/var/run/sshd.pid','start': None, 'stop': None},
	'Exim4': {'pidfile': '/var/run/exim4/eximqr.pid','start': None, 'stop': None},
	'Cron': {'pidfile': '/var/run/crond.pid','start': None, 'stop': None},
	}

CONFIG={'TMP_DIR': '/tmp/', }
