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

def set(section, option, value):
    """Set a setting in the configuration"""
    config = configparser.RawConfigParser()
    config.readfp(open('/etc/hippocp/hippocp.conf'))
    cfgfile = open("/etc/hippocp/hippocp.conf",'w')
    try:
        config.set(section, option, value)
        config.write(cfgfile)
        cfgfile.close()
    except configparser.NoSectionError:
        # Create non-existent section
        config.add_section(section)
        config.write(cfgfile)
        cfgfile.close()
        set(section, option, value)