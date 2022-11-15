from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class OpenetsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'openets'
    verbose_name = _('Open Event Ticketing System')
