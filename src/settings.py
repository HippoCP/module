import configparser
import os

def get(section, option):
	"""Retrive a configuration setting.

	Keywords arguments:
	section -- the section in which we are looking for
	option -- the option we are wondering about
	"""
	config = configparser.ConfigParser()
	config.readfp(open('/etc/hippocp/hippocp.conf'))
	try: 
		return config.get(section, option)
	except (configparser.NoSectionError, configparser.NoOptionError):
		return None
