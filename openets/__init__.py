from django.utils.version import get_version

VERSION = (1, 0, 0, 'alpha', 0)

__version__ = get_version(VERSION)

default_app_config = 'openets.apps.OpenetsConfig'
